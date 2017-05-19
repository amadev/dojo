class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        A = A.upper()
        k = len(A) - 1
        n = 0
        for i in range(k, -1, -1):
            v = ord(A[i]) - 64
            n += v * (26 ** (k - i))
        return n




s  = Solution()
print s.titleToNumber('z')
print s.titleToNumber('a')
print s.titleToNumber('aa')
print s.titleToNumber('ac')
print s.titleToNumber('az')
print s.titleToNumber('zz')
print s.titleToNumber('abc')
