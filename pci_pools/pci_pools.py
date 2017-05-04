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
# - mark each pci device pool with request
# - filter non unique tags
# - pick pci device pool for each request

def match_pool(pool, request):
    for i, v in enumerate(pool):
        if request[i] is None:
            continue
        if request[i] != v:
            return False
    return True


def filter_pools(lst):
    s = [set() for i in range(len(lst[0][0]))]
    def check_and_add(item):
        print 'item', item, 's', s
        for i in range(2):
            if item[i] in s[i]:
                return False
        for i in range(2):
            s[i].add(item[i])
        return True

    return [item for item in lst if check_and_add(item[0])]


def main(pools, requests):
    marked_pools = []
    for p in pools:
        mp = [p]
        for r in requests:
            if match_pool(p, r):
                mp.append(r)
        marked_pools.append(mp)
    filtered_pools = filter_pools(marked_pools)
    return filtered_pools

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
