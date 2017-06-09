class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        A = int(A)
        if A < 1:
            return 0
        while A > 0:
            if A & 1:
                return 0
            A = A >> 1
            if A == 1:
                break
        return 1

s = Solution()
assert 0 == s.power(0)
assert 0 == s.power(1)
assert 1 == s.power(2)
assert 0 == s.power(14)
assert 1 == s.power(16)
assert 1 == s.power(128)
assert 1 == s.power(2 ** 65)
assert 0 == s.power(2 ** 65 + 1)
