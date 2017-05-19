class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sign = A > 0
        A = abs(A)
        v = int(''.join(reversed(str(A))))
        if not sign:
            v = -v
        if v < (- 2 ** 31) or v > (2 ** 31 - 1):
            return 0
        return v

s = Solution()
assert 321 == s.reverse(123)
assert -321 == s.reverse(-123)
assert 0 == s.reverse(-1146467285)
assert 0 == s.reverse(0)
