class Solution:
    def isp(self, A, s, e):
        while s < e:
            if A[s] != A[e]:
                return False
            s += 1
            e -= 1
        return True
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        for i in range(n - 1, -1, -1):
            if self.isp(A, 0, i):
                return n - i - 1

s = Solution()
assert 2 == s.solve('ABC')
assert 5 == s.solve('banana')
