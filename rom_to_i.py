class Solution:
    # @param A : string
    # @return an integer
    def romanToInt(self, A):
        n = len(A)
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        r = 0
        for i in xrange(n):
            r += m[A[i]]
            if i < n - 1 and m[A[i + 1]] > m[A[i]]:
                r -= 2 * m[A[i]]
        return r

s = Solution()
assert 14 == s.romanToInt('XIV')
assert 79 == s.romanToInt('LXXIX')
assert 1954 == s.romanToInt('MCMLIV')
assert 1990 == s.romanToInt('MCMXC')
