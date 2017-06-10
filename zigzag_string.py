class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        n = len(A)
        r = []
        if B == 1:
            return A
        for i in range(B):
            j = i
            if i == (B - 1):
                s = (B - 2) * 2 + 1
            else:
                si = s = (B - i - 2) * 2 + 1
            d = False
            while j < n:
                # print i, j, s
                r.append(A[j])
                j += s + 1
                d = not d
                if i != 0 and i != (B - 1):
                    if d == True:
                        s = (i - 1) * 2 + 1
                    else:
                        s = si

        # print r, len(r)
        return ''.join(r)

s = Solution()
assert '' == s.convert('', 5)
assert 'ABCD' == s.convert('ABCD', 1)
assert 'ACBD' == s.convert('ABCD', 2)
assert 'ABDC' == s.convert('ABCD', 3)
assert 'PAHNAPLSIIGYIR' == s.convert('PAYPALISHIRING', 3)
assert 'A' * 10 == s.convert('A' * 10, 5)
assert 'A' * 100 == s.convert('A' * 100, 11)
assert 'AIBHJCGDFE' == s.convert('ABCDEFGHIJ', 5)
assert 'AGMSY5BFHLNRTXZ460CEIKOQUW1379DJPV28' == s.convert('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 4)
