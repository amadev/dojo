# Search in [imin, imax]:
#     i = (imin + imax) / 2
#     j = ((m + n + 1) / 2) - i
#     if B[j - 1] > A[i]:
#         search in [i + 1, imax]
#     else if A[i - 1] > B[j]:
#         search in [imin, i - 1]
#     else:
#         if m + n is odd:
#             answer is max(A[i - 1], B[j - 1])
#         else:
#             answer is (max(A[i - 1], B[j - 1]) + min(A[i], B[j])) / 2




class Solution:

    def med(self, X):
        n = len(X)
        if n & 1:
            return X[n/2]
        return (X[n/2 - 1] + X[n/2]) / 2.

    def merge(self, A, B):
        n = len(A)
        m = len(B)
        i = j = 0
        r = []
        while i < n and j < m:
            a = A[i]
            b = B[j]
            if a < b:
                r.append(a)
                i += 1
            else:
                r.append(b)
                j += 1
        r.extend(A[i:])
        r.extend(B[j:])
        return r

    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        r = self.merge(A, B)
        return self.med(r)

s = Solution()
assert 2.5 == s.findMedianSortedArrays([], [1, 2, 3, 4])
assert 1.5 == s.findMedianSortedArrays([1], [2])
assert 2.5 == s.findMedianSortedArrays([1], [2, 3, 5])
assert 3 == s.findMedianSortedArrays([1], [2, 3, 5, 6])
assert 2.5 == s.findMedianSortedArrays([1, 2], [3, 4])
assert 3 == s.findMedianSortedArrays([1, 2], [3, 4, 5])
assert 3.5 == s.findMedianSortedArrays([1, 2], [3, 4, 5, 6])
assert 3.5 == s.findMedianSortedArrays([1, 2, 3], [4, 5, 6])
assert 4 == s.findMedianSortedArrays([1, 2, 3, 5], [4, 7, 8])
assert -10 == s.findMedianSortedArrays([ -43, -25, -18, -15, -10, 9, 39, 40 ], [ -2 ])
assert -5.5 == s.findMedianSortedArrays([ 50 ],  [ -31, -26, -23, -15, -8, -3, 16, 23, 29 ])
