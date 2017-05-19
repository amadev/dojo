import math

class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        base = 26
        r = []
        while A > 0:
            rem = A % base
            A /= base
            if rem == 0:
                rem = base
                A -= 1
            r.insert(0, rem)
        return ''.join(map(lambda x: chr(x + 64), r))

s = Solution()
print s.convertToTitle(1)
print s.convertToTitle(25)
print s.convertToTitle(26)
print s.convertToTitle(27)
print s.convertToTitle(28)
print s.convertToTitle(52)
print s.convertToTitle(702)
print s.convertToTitle(731)
