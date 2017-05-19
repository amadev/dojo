def get(t, i):
    if i < 0:
        return 0
    try:
        return t[i]
    except IndexError:
        return 0

class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        prev = [1]
        if A == 0:
            return prev
        for i in xrange(1, A + 1):
            curr = [0] * (i + 1)
            for j in xrange(i + 1):
                curr[j] = get(prev, j - 1) + get(prev, j)
            prev = curr
        return curr

s = Solution()
print s.getRow(0)
print s.getRow(1)
print s.getRow(2)
print s.getRow(3)
print s.getRow(4)
