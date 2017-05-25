class Solution:
    # @param A : integer
    # @return a boolean
    def isPower(self, A):
        for i in range(2, 32):
            v = round(A ** (1.0 / i), 4)
            if v % int(v) == 0:
                return 1
        return 0


s = Solution()
assert 1 == s.isPower(823543)
