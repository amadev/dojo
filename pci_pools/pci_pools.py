# problem: we have pci devices grouped into pools, each pool has own
# set of properties or tags. While requesting the particular pci
# device we need to pick it according to pci request tags which have to
# be matched with pci pools tags. After that, we need to get pci device
# pools with unique values for specified tags. Unique values mean no
# value should be same for each tag.

# input: list of pci device pools with tags, for simplicity pci device
# pool and pci requests are represented as dict
# output: updated pci requests with tags for picking particular pci devices

# example: see tests.py

# idea:
# - mark each pci device pool with request, if pool device satisfies
# several requests several duplicate pools will be added
# - go through all combinations of pci pools to find unique pool for each
# request, in the worst case it takes P!/(R!*(P!-R!)), where P is
# number of pools on compute node and R is number of pci requests
# for 256 pools and 2 requests it takes 32640 steps (quick enough)
# for 256 pools and 3 requests it takes 2763520 steps (quick enough)
# for 4 simultaneous requests it takes 174792640 steps (several tens
# of seconds) which is not acceptable. An actual number of pools
# definitely should be much lower, and for example for 16 pci pools
# it's quick enough for any number of requests
# - last step in to update initial pci requests with appropriate tag values

import itertools


def match_pool(pool, request):
    for k in request:
        if request[k] != pool.get(k, None):
            return False
    return True


def check_distinct_tag_values(lst):
    s = {k: set() for k in lst[0]}
    for item in lst:
        for k in item:
            if item[k] in s[k]:
                return False
        for k in item:
            s[k].add(item[k])
    return True


def filter_tags(pool, distinct_tags):
    return {t: pool[t] for t in pool if t in distinct_tags}


def pick(pools, requests, distinct_tags):
    marked_pools = []
    for p in pools:
        for i in range(len(requests)):
            if match_pool(p, requests[i]):
                p = filter_tags(p, distinct_tags)
                p['request'] = i
                marked_pools.append(p)
    for pools_list in itertools.combinations(marked_pools, len(requests)):
        if check_distinct_tag_values(pools_list):
            for pool in pools_list:
                req_num = pool['request']
                del pool['request']
                requests[req_num].update(pool)
            return requests
    return None
