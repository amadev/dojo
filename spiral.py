# name: return all elements of a matrix in spiral order
# input: 2-d array
# output: list in spiral order
# idea: |
#   we have direction variable (r,d,l,u) and borders for each
#   side, in cycle from 0 to m * n we will change direction if we hit
#   border and at the same time border for the side is decremented

class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        R = len(A)
        C = len(A[0])
        i = j = 0
        d = 'r'
        borders = [0, 0, C - 1, R - 1]
        res = []
        for k in range(R * C):
            res.append(A[i][j])
            if d == 'r':
                if j < borders[2]:
                    j += 1
                else:
                    d = 'd'
                    borders[2] -= 1
            if d == 'd':
                if i < borders[3]:
                    i += 1
                else:
                    d = 'l'
                    borders[3] -= 1
            if d == 'l':
                if j > borders[0]:
                    j -= 1
                else:
                    d = 'u'
                    borders[0] += 1
                    borders[1] += 1
            if d == 'u':
                if i > borders[1]:
                    i -= 1
                else:
                    d = 'r'
                    j += 1
        return res

s = Solution()
assert [1, 2, 3, 6, 9, 8, 7, 4, 5] == s.spiralOrder([[1, 2, 3],
                                                     [4, 5, 6],
                                                     [7, 8, 9]])

assert [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10] == \
        s.spiralOrder([[ 1, 2, 3, 4],
                       [ 5, 6, 7, 8],
                       [ 9,10,11,12],
                       [13,14,15,16]])
