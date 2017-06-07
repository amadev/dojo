class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        n = len(A)
        l = 0
        h  = n - 1
        while l <= h:
            m = (l + h) / 2
            if B == A[m]:
                return m
            elif B < A[m]:
                h = m - 1
            else:
                l = m + 1
        return l


s = Solution()
assert 1 == s.searchInsert([2, 4], 3)
assert 0 == s.searchInsert([], 1)
assert 2 == s.searchInsert([1,3,5,6], 5)
assert 1 == s.searchInsert([1,3,5,6], 2)
assert 4 == s.searchInsert([1,3,5,6], 7)
assert 0 == s.searchInsert([1,3,5,6], 0)
