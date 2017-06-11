class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        i = 31
        r = 0
        while A:
            if A & 1:
                r = r | (1 << i)
            i -= 1
            A = A >> 1
        return r

s = Solution()
assert 4294967295 == s.reverse(4294967295)
assert 2147483648 == s.reverse(1)
