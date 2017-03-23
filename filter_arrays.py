
cases = [
    [
        [], []
    ],
    [
        [[1], [1]], [[1]]
    ],
    [
        [[1, 2], [1, 3]], [[1, 2]]
    ],
    [
        [[1, 2, 3], [2, 2, 3], [2, 3, 3], [2, 3, 4]], [[1, 2, 3], [2, 3, 4]]
    ],
]


def get_unique_arrays(lst):
    s = [set() for i in range(len(lst))]

    def check_and_add(item):
        for i, value in enumerate(item):
            if value in s[i]:
                return False
        for i, value in enumerate(item):
            s[i].add(value)
        return True

    return [item for item in lst if check_and_add(item)]


for case in cases:
    assert get_unique_arrays(case[0]) == case[1], \
        'fail on case %s | result: %s' % (case, get_unique_arrays(case[0]))
