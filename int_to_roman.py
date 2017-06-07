class Solution:
    # @param A : integer
    # @return a strings
    def intToRoman(self, A):
        m = {
            1: 'I',
            2: 'II',
            3: 'III',
            4: 'IV',
            5: 'V',
            6: 'VI',
            7: 'VII',
            8: 'VIII',
            9: 'IX',
            10: 'X',
            20: 'XX',
            30: 'XXX',
            40: 'XL',
            50: 'L',
            60: 'LX',
            70: 'LXX',
            80: 'LXXX',
            90: 'XC',
            100: 'C',
            200: 'CC',
            300: 'CCC',
            400: 'CD',
            500: 'D',
            600: 'DC',
            700: 'DCC',
            800: 'DCCC',
            900: 'CM',
            1000: 'M',
            2000: 'MM',
            3000: 'MMM'
        }
        A = str(A)
        n = len(A)
        r = []
        for i in range(n):
            r.append(int(A[i] + ''.join(['0'] * (n - i - 1))))
        return ''.join(map(lambda x: m[x], filter(lambda x: x != 0, r)))


s = Solution()
assert '' == s.intToRoman(0)
assert 'I' == s.intToRoman(1)
assert 'II' == s.intToRoman(2)
assert 'III' == s.intToRoman(3)
assert 'IV' == s.intToRoman(4)
assert 'V' == s.intToRoman(5)
assert 'VI' == s.intToRoman(6)
assert 'VII' == s.intToRoman(7)
assert 'VIII' == s.intToRoman(8)
assert 'IX' == s.intToRoman(9)
assert 'X' == s.intToRoman(10)
assert 'XXI' == s.intToRoman(21)
assert 'XXIII' == s.intToRoman(23)
assert 'XL' == s.intToRoman(40)
assert 'XC' == s.intToRoman(90)
assert 'XIX' == s.intToRoman(19)
assert 'MCMLIV' == s.intToRoman(1954)
# for i in range(1, 4000):
#     assert  i == romanToInt(s.intToRoman(i))
