class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        while B > 0:
            t = B
            B = A % B
            A = t
        return A

s = Solution()
print s.gcd(6, 12)
print s.gcd(6, 9)
