class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        n = len(A)
        j = 0
        for i in range(n):
            if A[i] != B:
                A[j] = A[i]
                j += 1
            print A[i], i, j
        return A, j

s = Solution()
assert ([], 0) == s.removeElement([1, 1, 1], 1)
assert ([2], 1) == s.removeElement([1, 1, 1, 2], 1)
assert ([1, 1, 1], 3) == s.removeElement([1, 1, 1, 2], 2)
assert ([2, 3, 4, 5, 7, 8], 6) == s.removeElement([1, 1, 2, 3, 4, 1, 5, 7, 1, 1, 8, 1], 1)g
