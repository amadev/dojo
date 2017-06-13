class Solution:
    def med(self, X):
        n = len(X)
        if n & 1:
            return X[n/2]
        return (X[n/2 - 1] + X[n/2]) / 2.

    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if not m:
            return self.med(B)
        if not n:
            return self.med(A)

        def search(imin, imax):
            print 'imin, imax', imin, imax
            i = (imin + imax) / 2
            j = ((m + n + 1) / 2) - i
            print 'i, j', i, j
            if B[j - 1] > A[i]:
                return search(i + 1, imax)
            elif A[i - 1] > B[j]:
                return search(imin, i - 1)
            else:
                if (m + n) & 1:
                    return max(A[i - 1], B[j - 1])
                else:
                    return (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2.
        return search(0, m)



s = Solution()
#assert 6.5 == s.findMedianSortedArrays([1, 4, 6, 8, 10], [5, 7, 9])
# assert 2.5 == s.findMedianSortedArrays([], [1, 2, 3, 4])
assert 1.5 == s.findMedianSortedArrays([1], [2])
# assert 2.5 == s.findMedianSortedArrays([1], [2, 3, 5])
# assert 3 == s.findMedianSortedArrays([1], [2, 3, 5, 6])
# assert 2.5 == s.findMedianSortedArrays([1, 2], [3, 4])
# assert 3 == s.findMedianSortedArrays([1, 2], [3, 4, 5])
# assert 3.5 == s.findMedianSortedArrays([1, 2], [3, 4, 5, 6])
# assert 3.5 == s.findMedianSortedArrays([1, 2, 3], [4, 5, 6])
# assert 4 == s.findMedianSortedArrays([1, 2, 3, 5], [4, 7, 8])
# assert -10 == s.findMedianSortedArrays([ -43, -25, -18, -15, -10, 9, 39, 40 ], [ -2 ])
# assert -5.5 == s.findMedianSortedArrays([ 50 ],  [ -31, -26, -23, -15, -8, -3, 16, 23, 29 ])
