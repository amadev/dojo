class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A)
        layers = n / 2
        length = n - 1
        for l in range(layers):
            for i in range(l, length - l):
                temp = A[l][i]
                A[l][i] = A[length - i][l]
                A[length - i][l] = A[length - l][length - i]
                A[length - l][length - i] = A[i][length - l]
                A[i][length - l] = temp
        return A

s = Solution()
assert [[3, 1], [4, 2]] == s.rotate([[1, 2],
                                     [3, 4]])

assert [] == s.rotate([])
assert [1] == s.rotate([1])
