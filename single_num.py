class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        if not A:
            return -1
        return reduce(lambda a, b: a ^ b, A)

s = Solution()
assert 3 == s.singleNumber([1,2,2,3,1])
assert 1 ==  s.singleNumber([1])
