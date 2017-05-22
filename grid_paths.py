# public int uniquePaths(int m, int n) {
#     if(m==0 || n==0) return 0;
#     if(m==1 || n==1) return 1;

#     int[][] dp = new int[m][n];

#     //left column
#     for(int i=0; i<m; i++){
#         dp[i][0] = 1;
#     }

#     //top row
#     for(int j=0; j<n; j++){
#         dp[0][j] = 1;
#     }

#     //fill up the dp table
#     for(int i=1; i<m; i++){
#         for(int j=1; j<n; j++){
#             dp[i][j] = dp[i-1][j] + dp[i][j-1];
#         }
#     }

#     return dp[m-1][n-1];
# }


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
