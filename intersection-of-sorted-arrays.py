class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def intersect(self, A, B):
        i = j = 0
        n = len(A)
        m = len(B)
        r = []
        while i < n and j < m:
            a = A[i]
            b = B[j]
            if b < a:
                j += 1
            elif b == a:
                r.append(a)
                i += 1
                j += 1
            else:
                i += 1
        return r

s = Solution()
assert [] == s.intersect([1, 2, 3, 5, 5], [6, 7])
assert [1, 1, 1] == s.intersect([1, 1, 1], [1, 1, 1])
assert [5, 5] == s.intersect([1, 2, 3, 5, 5], [5, 5, 6])
