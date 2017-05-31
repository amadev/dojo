class Solution:

    def bs(self, A, B, first):
        n = len(A)
        s = 0
        e = n - 1
        r = -1
        while s <= e:
            m = (s + e) / 2
            if B == A[m]:
                r = m
                if first:
                    e = m - 1
                else:
                    s = m + 1
            elif B < A[m]:
                e = m - 1
            else:
                s = m + 1
        return r
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        s = self.bs(A, B, True)
        if s == -1:
            return [-1, -1]
        return [s, self.bs(A, B, False)]


s = Solution()
assert [3, 4] ==  s.searchRange([5, 7, 7, 8, 8, 10], 8)
assert [1, 2] ==  s.searchRange([5, 7, 7, 8, 8, 10], 7)
assert [-1, -1] ==  s.searchRange([5, 7, 7, 8, 8, 10], 4)
