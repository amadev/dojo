class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        if A < 2:
            return []
        p = [1] * (A + 1)
        p[0] = 0
        p[1] = 0
        for i in range(2, int(A ** 0.5) + 1):
            if p[i] == 1:
                j = 2
                while i * j <= A:
                    p[i * j] = 0
                    j += 1
        return [i for i in range(A + 1) if p[i]]

s = Solution()
assert [2] ==  s.sieve(2)
assert [2, 3, 5, 7] == s.sieve(7)
assert [] == s.sieve(0)
