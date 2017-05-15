class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        A = list(A)
        R = len(A)
        if R == 0:
            return []
        C = len(A[0])
        R0 = 1 if all(A[0][j] == 1 for j in range(C)) else 0
        C0 = 1 if all(A[i][0] == 1 for i in range(R)) else 0
        for i in range(1, R):
            A[i][0] = 1 if all(A[i][j] == 1 for j in range(C)) else 0
        for j in range(1, C):
            A[0][j] = 1 if all(A[i][j] == 1 for i in range(R)) else 0
        for i in range(1, R):
            for j in range(1, C):
                if A[i][0] == 0 or A[0][j] == 0:
                    A[i][j] = 0
        if R0 == 0:
            for j in range(C):
                A[0][j] = 0
        if C0 == 0:
            for i in range(R):
                A[i][0] = 0
        return A


s = Solution()
# prnit s.setZeroes([[0, 0], [1, 1]])
# print s.setZeroes([])
# print s.setZeroes([[0, 0, 0]])
# print s.setZeroes([[1, 1, 1]])
# print s.setZeroes([[1, 0, 1],
#                    [1, 1, 1],
#                    [1, 1, 1]])


# print s.setZeroes(
# [
#     [1, 1],
#     [0, 0],
# ])



print s.setZeroes(
    [
        [1, 1],
        [1, 0]
])
