class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        if len(A) > len(B):
            return self._addBinary(A, B)
        return self._addBinary(B, A)

    def _addBinary(self, A, B):
        n = len(A)
        m = len(B)
        r = []
        rem = 0
        for i in range(1, n + 1):
            a = int(A[-i])
            if i > m:
                b = 0
            else:
                b = int(B[-i])
            c = a + b + rem
            if c == 2:
                c = 0
                rem = 1
            elif c == 3:
                c = 1
                rem = 1
            else:
                rem = 0
            r.insert(0, str(c))
        if rem == 1:
            r.insert(0, '1')
        return ''.join(r)


s = Solution()
assert '111' == s.addBinary('100', '11')
assert '110' == s.addBinary('11', '11')
assert '0' == s.addBinary('0', '0')
assert '' == s.addBinary('', '')
assert '10' == s.addBinary('1', '1')
assert '10000' == s.addBinary('1', '1111')
