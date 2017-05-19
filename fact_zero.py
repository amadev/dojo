import math

class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        if A < 5:
            return 0
        n = int(math.log(A, 5))
        c = 0
        for i in range(1, n + 1):
            c += A / 5 ** i
        return c
