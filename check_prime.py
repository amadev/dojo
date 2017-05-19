class Solution:
    # @param A : integer
    # @return an integer
    def isPrime(self, A):
        if A == 1:
            return 0
        upperLimit = int(A**0.5)
        for i in xrange(2, upperLimit + 1):
            if i < A and A % i == 0:
                return 0
        return 1


s = Solution()
print s.isPrime(2)
