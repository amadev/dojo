class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        l = 1
        h = A
        mx = 0
        while l <= h:
            m = (l + h) / 2
            mm = m * m
            if mm == A:
                return m
            elif mm < A:
                l = m + 1
                mx = max(mx, m)
            else:
                h = m - 1
        return mx

s = Solution()
assert 0 == s.sqrt(0)
assert 1 == s.sqrt(1)
assert 1 == s.sqrt(2)
assert 1 == s.sqrt(3)
assert 2 == s.sqrt(4)
assert 3 == s.sqrt(9)
assert 3 == s.sqrt(11)
assert 3 == s.sqrt(15)
assert 4 == s.sqrt(16)
assert 16 == s.sqrt(256)
assert 16 == s.sqrt(256)

for i in range(1000):
    assert int(i ** 0.5) == s.sqrt(i), i
