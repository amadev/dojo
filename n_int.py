class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        for i in range(n):
            d = n - i - 1
            j = i + 1
            while j < n and A[j] == A[i]:
                d -= 1
                j += 1
            if A[i] == d:
                return A[i]
        return -1

s = Solution()
print s.solve([1, 2, 2, 4])
