def get(t, i, j):
    if j < 0 or j < 0:
        return 0
    try:
        return t[i][j]
    except IndexError:
        return 0


class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0:
            return []
        t = [[1]]
        for i in range(1, A):
            K = i + 1
            t.append([0] * K)
            for j in range(K):
                t[i][j] = get(t, i - 1, j) + get(t, i - 1, j - 1)
        return t


s = Solution()
print s.generate(0)
print s.generate(5)
