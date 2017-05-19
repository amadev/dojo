class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        sqrt = int(A ** 0.5)
        ans = []
        ends = []
        for i in range(1, sqrt + 1):
            if A % i == 0:
                ans.append(i)
                if A / i != sqrt:
                    ends.insert(0, A / i)
        return ans + ends

s = Solution()
print s.allFactors(6)
print s.allFactors(6)
print s.allFactors(3)
print s.allFactors(0)
print s.allFactors(100)
print s.allFactors(25)
