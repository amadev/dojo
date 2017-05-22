# problem: |
#   There is grid, size is RxC and robot can go only down and right.
#   Find number of unique path to the most right-down cell.
# input: int R, int C
# output: int
# idea: |
#   for first row and column number of paths for each cell is 1,
#   for cell 2,2 = cell 1,2 + cell 2,1 and so on

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        if A == 0 or B == 0:
            return 0
        if A == 1 or B == 1:
            return 1
        dp = []
        for i in range(A):
            dp.append([0] * B)
        for i in range(A):
            dp[i][0] = 1
        for j in range(B):
            dp[0][j] = 1
        for i in range(1, A):
            for j in range(1, B):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[A - 1][B - 1]


s = Solution()
assert 2 == s.uniquePaths(2, 2)
