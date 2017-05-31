import math

class Solution:

    def inds(self, x, n, m):
        i = int(math.ceil(x / float(m))) - 1
        j = (x % m) - 1
        if j == -1:
            j = m - 1
        return i, j


    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        if not A:
            return 0
        n = len(A)
        m = len(A[0])
        s = 0
        e = m * n
        while s <= e:
            mid = (s + e) / 2
            i, j = self.inds(mid, n, m)
            if A[i][j] == B:
                return 1
            elif B < A[i][j]:
                e = mid - 1
            else:
                s = mid + 1
        return 0

s = Solution()
assert 1 == s.searchMatrix(
    [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 3
)

assert 0 == s.searchMatrix(
    [
        [1,   3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ], 4
)

assert 0 == s.searchMatrix(
[
    [2, 9, 12, 13, 16, 18, 18, 19, 20, 22],
    [29, 59, 62, 66, 71, 75, 77, 79, 97, 99]
], 45)

assert 1 == s.searchMatrix(
    [
        [3, 3, 11, 12, 14],
        [16, 17, 30, 34, 35],
        [45, 48, 49, 50, 52],
        [56, 59, 63, 63, 65],
        [67, 71, 72, 73, 79],
        [80, 84, 85, 85, 88],
        [88, 91, 92, 93, 94],
    ],

94)

assert 1 == s.searchMatrix(
    [
        [5, 6, 6, 10, 11, 12, 12, 12, 15, 16],
        [18, 18, 19, 21, 21, 21, 22, 22, 23, 24],
        [29, 32, 32, 32, 33, 34, 34, 34, 35, 40],
        [40, 42, 42, 43, 44, 46, 46, 47, 47, 47],
        [48, 48, 48, 50, 51, 51, 51, 51, 51, 52],
        [53, 56, 57, 59, 59, 60, 61, 61, 61, 63],
        [63, 64, 64, 65, 65, 65, 67, 67, 67, 67],
        [70, 73, 74, 74, 74, 75, 75, 79, 79, 81],
        [82, 83, 83, 84, 84, 85, 86, 88, 89, 91],
        [91, 91, 95, 95, 96, 96, 97, 99, 100, 100],
    ],96
)
 #print s.inds(8, 3, 4)
