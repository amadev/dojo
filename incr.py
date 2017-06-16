class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        if any(i < 0 or not isinstance(i, (int, long)) for i in A):
            return []
        n = len(A)
        i = 0
        for i in xrange(n):
            if A[i] != 0:
                break
        A = A[i:]
        n -= i
        if n == 0:
            return [1]
        for i in xrange(n - 1, -1, -1):
            if A[i] < 9:
                A[i] += 1
                break
            A[i] = 0
            if i == 0:
                A.insert(0, 1)
        return A

s = Solution()
assert [4, 4, 6, 0, 9, 6, 5, 2] == s.plusOne([ 0, 0, 4, 4, 6, 0, 9, 6, 5, 1 ])
assert [1] == s.plusOne([])
assert [2] == s.plusOne([1])
assert [2, 0] == s.plusOne([0, 1, 9])
assert [1, 0, 0, 0] == s.plusOne([9, 9, 9])
assert [] == s.plusOne([-1, -1, -1])
assert [] == s.plusOne(['a'])
