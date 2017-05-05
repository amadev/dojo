# problem: we have pci devices grouped into pools, each pool has own set
# of properties or tags. While requesting particular pci device we need
# pick it according to pci request tags which have to be matched with
# pci pools tags. After that we need to get pci device pools with unique
# values for specified tags. Unique values mean no value should be same
# for each tag.

# input: list of pci device pools with tags, for simplicity pci device
# pool is represented as array where elements are tag values.
# output: list of tags should be added to each pci request to pick pci
# devices with unique tags

# example:
# we have the following pools:
# p1 [1, 3, 1]
# p2 [2, 3, 1]
# p3 [1, 4, 2]
# p4 [2, 3, 2]
# we have two pci requests r1 where thid pool tag should be equal to 1
# and r2 where thid pool tag should be equal to 2.
# first and second tags for selected pci device have to be unique
# as result updated pci request must be r1 [2, 3, 1], r2 [1, 4, 2]

# idea:
# - mark each pci device pool with request, if pool device satisfies
# several requests several duplicate pools will be added
# - go through all combinations of pci pools to find unique for each
# request it takes P!/(R!*(P!-R!))
# for 256 pools and 2 requests it takes 32640 steps (quick enough)
# for 256 pools and 3 requests it takes 2763520 steps (quick enough)
# for 4 simultanious requests it takes 174792640 steps (several tens
# of seconds) which is not acceptable. Actual number of pools
# definitely should be much lower, and for example for 16 pci pools
# it's quick enough for any numeber of requests


import itertools


def match_pool(pool, request):
    for i, v in enumerate(pool):
        if request[i] is None:
            continue
        if request[i] != v:
            return False
    return True


def check_unique_tags(lst):
    n = len(lst[0])
    s = [set() for i in range(n)]
    for item in lst:
        for i in range(n):
            if item[i] in s[i]:
                return False
        for i in range(n):
            s[i].add(item[i])
    return True


def filter_tags(p):
    return p[0:2]


def main(pools, requests):
    marked_pools = []
    for p in pools:
        for i in range(1, len(requests) + 1):
            if match_pool(p, requests[i - 1]):
                p = filter_tags(p)
                p.append('r%s' % i)
                marked_pools.append(p)
    for p in itertools.combinations(marked_pools, len(requests)):
        if check_unique_tags(p):
            return p
    return None

pools = [
    [1, 3, 1],
    [2, 3, 1],
    [1, 4, 2],
    [2, 3, 2]
]

requests = [
    [None, None, 1],
    [None, None, 2]
]

print main(pools, requests)
