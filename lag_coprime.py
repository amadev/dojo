class Solution:

    def gcd(self, A, B):
        while B > 0:
            t = B
            B = A % B
            A = t
        return A

    # @param A : integer
    # @param B : integer
    # @return an integer
    def cpFact(self, A, B):
        gcd = self.gcd(A, B)
        while gcd != 1:
            A /= gcd
            gcd = self.gcd(A, B)
        return A


s = Solution()
assert 5 == s.cpFact(30, 12)
