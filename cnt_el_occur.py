class Solution:
    def binarySearch(self, A, B, first=True):
        s = 0
        e = len(A) - 1
        n = len(A)
        r = -1
        while s <= e:
            m = (e + s) / 2
            if A[m] == B:
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
    # @return an integer
    def findCount(self, A, B):
        l = self.binarySearch(A, B, False)
        if l == -1:
            return 0
        return l - self.binarySearch(A, B, True) + 1


s = Solution()
assert 2 == s.findCount([5, 7, 7, 8, 8, 10], 7)
