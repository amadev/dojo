class Solution:
    def _s(self, A, B):
        n = len(A)
        m = len(B)
        rem = 0
        for i in range(1, m + 1):
            b = int(B[-i])
            if i > n:
                a = 0
            else:
                a = int(A[-i])
            c = a + b + rem


    def s(self, a, b):
        return str(int(a) + int(b))
        n = len(a)
        m = len(b)
        if n > m:
            return self._s(a, b)
        return self._s(b, a)

    def m(self, A, B):
        n = len(A)
        m = len(B)
        print A, B
        r = []
        for i in range(1, m + 1):
            t = [0] * (i - 1)
            b = int(B[-i])
            rem = 0
            for j in range(1, n + 1):
                a = int(A[-j])
                c = a * b + rem
                rem = 0
                if c > 9:
                    rem = c / 10
                    c = c % 10
                t.insert(0, c)
            if rem:
                t.insert(0, rem)
            r.append(''.join(map(str, t)))
        if len(r) == 1:
            return r[0]
        return reduce(self.s, r)

    def rlz(self, x):
        i = 0
        for i in range(len(x)):
            if x[i] != '0':
                break
        return x[i:]


    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        A = self.rlz(A)
        B = self.rlz(B)
        n = len(A)
        m = len(B)
        if not n or not m:
            return '0'
        if A == '0' or B == '0':
            return '0'
        if n > m:
            return self.m(A, B)
        return self.m(B, A)



s = Solution()
assert '0' == s.multiply('00001', '')
assert '1' == s.multiply('00001', '001')
assert str(123 * 57) == s.multiply('123', '57')
assert '0' == s.multiply('1', '0')

assert str(1234 * 5700) == s.multiply('01234', '005700')
assert str(1 * 5700) == s.multiply('01', '005700')
assert '0' == s.multiply('00', '005700')

# 290851027081985078955918627261751688832742312387314888842460711865148550965912482730570750031304678344564428861596637320
assert '290851027081985078955918627261751688832742312387314888842460711865148550965912482730570750031304678344564428861596637320' \
    == s.multiply("5131848155574784703269632922904933776792735241197982102373370",
                  '56675688419586288442134264892419611145485574406534291250836')

# assert str(5131848155574784703269632922904933776792735241197982102373370 *
#            56675688419586288442134264892419611145485574406534291250836) == '290851027081985078955918627261751688832742312387314888842460711865148550965912482730570750031304678344564428861596637320'
