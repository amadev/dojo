# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def maximumGap(self, A):
#         n = len(A)
#         if n == 0:
#             return 0
#         m = A[0]
#         arr = [0] * n
#         m_dist = 0
#         for i in range(n):
#             if A[i] > m:
#                 arr[i] = False
#             else:
#                 arr[i] = True
#                 m = A[i]
#         i = j = n - 1
#         while i >= 0:
#             if not arr[i]:
#                 i -= 1
#                 continue
#             while A[i] > A[j] and j > i:
#                 j -= 1
#             m_dist = max(m_dist, j - i)
#             i -= 1
#         return m_dist

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        n = len(A)
        for i in xrange(n):
            A[i] = (A[i], i)
        A.sort()
        print A
        m = 0
        for i in xrange(n - 1):
            print A[i + 1][1],   A[i][1]
            m = max(m, A[i + 1][1] - A[i][1])
        return m

s = Solution()
#assert 2 == s.maximumGap([3, 5, 4, 2])
assert 2 == s.maximumGap([ -1, -1, 2 ])
