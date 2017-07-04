class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        I = len(A)
        J = len(B)
        K = len(C)
        d = float('inf')
        inds = [0, 0, 0]
        while inds[0] < I and inds[1] < J and inds[2] < K:
            a = A[inds[0]]
            b = B[inds[1]]
            c = C[inds[2]]
            d = min(d, abs(max(a, b, c) - min(a, b, c)))
            vals = [a, b, c]
            inds[vals.index(min(vals))] += 1
        return d


s = Solution()
assert 1 == s.solve(
    [ 1, 4, 5, 8, 10 ],
    [ 6, 9, 15 ],
    [ 2, 3, 6, 6 ]
)
