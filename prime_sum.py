class Solution:
    # @param A : integer
    # @return a list of integers
    def sieve(self, A):
        if A < 2:
            return []
        p = [1] * (A + 1)
        p[0] = 0
        p[1] = 0
        for i in range(2, A + 1):
            if p[i] == 1:
                j = 2
                while i * j <= A:
                    p[i * j] = 0
                    j += 1
        r = []
        for i in range(A + 1):
            if p[i] == 1:
                r.append(i)
        return r

    def primesum(self, A):
        l = self.sieve(A)
        for i in l:
            for j in l:
                if i + j == A:
                    return i, j

s = Solution()
print s.primesum(4)
