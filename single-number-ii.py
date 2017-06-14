def bin2(x):
    return bin(x)[2:].zfill(8)


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ones = twos = threes = 0
        n = len(A)
        for i in range(n):
            print 'A[i]', bin2(A[i]), A[i]
            twos |= ones & A[i]
            print 'twos', bin2(twos), twos
            ones ^= A[i]
            print 'ones', bin2(ones), ones
            threes = ones & twos
            print 'threes', bin2(threes), threes
            ones &= ~threes
            print 'ones', bin2(ones), ones
            twos &= ~threes
            print 'twos', bin2(twos), twos
        return ones

s = Solution()
assert 4 == s.singleNumber([1, 2, 4, 3, 3, 2, 2, 3, 1, 1])
assert 1 == s.singleNumber([1])
