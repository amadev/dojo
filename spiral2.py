class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        dr = 'r'
        br = {'r': A - 1, 'l': 0, 'u': 0, 'd': A - 1}
        M = []
        for i in range(A):
            M.append([0] * A)
        i = j = 0
        for k in range(1, A ** 2 + 1):
            M[i][j] = k
            if dr == 'r':
                if j < br['r']:
                    j += 1
                else:
                    dr = 'd'
                    br['r'] -= 1
            if dr == 'd':
                if i < br['d']:
                    i += 1
                else:
                    dr = 'l'
                    br['d'] -= 1
            if dr == 'l':
                if j > br['l']:
                    j -= 1
                else:
                    dr = 'u'
                    br['l'] += 1
                    br['u'] += 1
            if dr == 'u':
                if i > br['u']:
                    i -= 1
                else:
                    dr = 'r'
                    j += 1
        return M


s = Solution()
print s.generateMatrix(3)
print s.generateMatrix(0)
print s.generateMatrix(4)
