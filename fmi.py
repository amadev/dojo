# todo compare alg efficiency

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        i = 0
        while i < n:
            if A[i] != i + 1:
                if A[i] <= 0 or A[i] > n:
                    i += 1
                    continue
                t = A[i] - 1
                tmp = A[t]
                A[t] = A[i]
                A[i] = tmp
            else:
                i += 1
        for i in range(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1


class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        n = len(A)
        for i in xrange(n):
            while A[i] != i + 1:
                if A[i] <= 0 or A[i] > n:
                    break
                t = A[i] - 1
                if A[i] == A[t]:
                    break
                tmp = A[i]
                A[i] = A[t]
                A[t] = tmp
        for i in xrange(n):
            if A[i] != i + 1:
                return i + 1
        return n + 1


s = Solution()
assert 2 == s.firstMissingPositive([1, 1, 1])
assert 1 == s.firstMissingPositive([])
assert 1 == s.firstMissingPositive([12])
assert 2 == s.firstMissingPositive([-1, -2, 1])
assert 3 == s.firstMissingPositive([1,2,0])
assert 2 == s.firstMissingPositive([3,4,-1,1])
assert 1 == s.firstMissingPositive([-1, -2, -3])
assert 4 == s.firstMissingPositive([1,2,3])
