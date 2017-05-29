import itertools


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        A = {i: i for i in A}
        C = map(int, str(C))
        a = len(A)
        if not a:
            return 0
        if B > len(C):
            return 0
        elif B < len(C):
            r = a ** (B - 1)
            if B > 1 and 0 in A:
                r *= a- 1
            else:
                r *= a
            return r
        dp = {1: len([i for i in A if i < C[0]])}
        if B == 1:
            return dp[1]
        if 0 in A:
            dp[1] -= 1
        lower = {}
        for v in C:
            lower[v] = len([k for k in A if k < v])
        for i in range(2, B + 1):
            dp[i] = a * dp[i - 1]
            if all(j in A for j in C[:i - 1]):
                dp[i] += lower[C[i - 1]]
        return dp[B]


def brf(A, B, C):
    cnt = 0
    for i in itertools.product(A, repeat=B):
        if B > 1 and i[0] == 0:
            continue
        if int(''.join(map(str, i))) < C:
            cnt += 1
    return cnt

s = Solution()
assert 4 == s.solve([0, 1, 2, 5], 1, 123)
assert 12 == s.solve([0, 1, 2, 5], 2, 210)
assert 0 == s.solve([0, 1, 2, 5], 2, 1)
assert 1 == s.solve([0], 1, 5)
assert 0 == s.solve([], 2, 2)
assert 2 == s.solve([0, 1, 2, 5], 1, 2)
assert 5 == s.solve([0, 1, 2, 5], 2, 21)
assert 23 == s.solve([0, 1, 2, 5], 3, 215)
assert 16 == s.solve([0, 1, 4, 5], 3, 215)
assert 0 == s.solve([2, 9], 5, 17015)
assert 12 == s.solve([ 2, 3, 5, 6, 7, 9 ], 2, 42)
assert 72 == s.solve([ 2, 3, 5, 6, 7, 9 ], 3, 429)

#assert brf([ 2, 3, 5, 6, 7, 9 ], 3, 429) == s.solve([ 2, 3, 5, 6, 7, 9 ], 3, 429)
assert 2592 == s.solve([ 2, 3, 5, 6, 7, 9 ], 5, 42950)
#print brf([0, 1, 4,  5], 3, 215)

assert 23040 == brf([ 0, 2, 3, 4, 5, 7, 8, 9 ], 5, 86587)
assert s.solve([ 0, 2, 3, 4, 5, 7, 8, 9 ], 5, 86587) == brf([ 0, 2, 3, 4, 5, 7, 8, 9 ],5, 86587)
