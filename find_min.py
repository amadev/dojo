class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        n = len(A)
        l = 0
        h = n - 1
        while l <= h:
            # print 'l,h', l, h
            # print 'A[l],A[h]', A[l], A[h]
            if A[l] <= A[h]:
                return A[l]
            m = (l + h) / 2
            ne = (m + 1) % n
            p = (m + n - 1) % n
            # print 'm, ne, p', m, ne, p
            # print 'A[m], A[ne], A[p]', A[m], A[p], A[ne]
            if A[m] <= A[p] and A[m] <= A[ne]:
                return A[m]
            if A[m] <= A[h]:
                h = m - 1
            elif A[m] >= A[l]:
                l = m + 1
        return -1


s = Solution()
assert 1 == s.findMin([5, 6, 7, 1, 2, 3])
