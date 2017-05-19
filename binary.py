class Solution:
    # @param A : integer
    # @return a strings
    def findDigitsInBinary(self, A):
        if A == 0:
            return '0'
        r = []
        while A >= 1:
            r.insert(0, A % 2)
            A = A / 2
        return ''.join(map(str, r))

s = Solution()
print s.findDigitsInBinary(7)
print s.findDigitsInBinary(0)
print s.findDigitsInBinary(1)
print s.findDigitsInBinary(10)
