class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return A modified after the merge
    def merge(self, A, B):
        n = len(A)
        m = len(B)
        r = []
        i = j = 0
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
        A[:] = r
        return A

s = Solution()
assert [] == s.merge([], [])
assert [1] == s.merge([1], [])
assert [1, 2, 3, 4] == s.merge([1, 2, 3], [4])
assert [1, 2, 3, 4, 5, 6] == s.merge([1, 4, 6], [2, 3, 5])
