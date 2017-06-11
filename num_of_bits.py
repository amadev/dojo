class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        cnt = 0
        while A > 0:
            if A & 1:
                cnt += 1
            A = A >> 1
        return cnt


s = Solution()
#print len(filter(lambda x: x == '1', '{0:b}'.format(100)))
assert 0 == s.numSetBits(0)
assert 1 == s.numSetBits(1)
assert 2 == s.numSetBits(5)
assert len(filter(lambda x: x == '1', '{0:b}'.format(100))) == s.numSetBits(100)
assert len(filter(lambda x: x == '1', '{0:b}'.format(555))) == s.numSetBits(555)
