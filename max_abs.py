A = [1, 3, -1]

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        if len(A) == 0:
            return 0
        m1 = m2 = m3 = m4 = - float("inf")
        for i in range(len(A)):
            m1 = max(m1, A[i] + i)
            m2 = max(m2, A[i] - i)
            m3 = max(m3, -A[i] + i)
            m4 = max(m4, -A[i] - i)
        m = - float("inf")
        for i in range(len(A)):
            m = max(m, m1 - (A[i] + i))
            m = max(m, m2 - (A[i] - i))
            m = max(m, m3 - (-A[i] + i))
            m = max(m, m4 - (-A[i] - i))
        return m

s = Solution()
assert 5 == s.maxArr(A), s.maxArr(A)
assert 0 == s.maxArr([])
assert 2 == s.maxArr([ 2, 2, 2 ])
