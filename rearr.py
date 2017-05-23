
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference.
    # You do not need to return anything in this case.
    def arrange(self, A):
        A = list(A)
        n = len(A)

        for i in range(n):
            A[i] += (A[A[i]] % n) * n

        print A
        for i in range(n):
            A[i] /= n

        return A

s = Solution()

# assert [0, 1] == s.arrange([1, 0])
# assert [1, 1, 1] == s.arrange([1, 1, 1])
# assert [0, 1, 2, 3] == s.arrange([3, 2, 1, 0])

assert [3, 4, 2, 0, 1]  ==s.arrange([ 4, 0, 2, 1, 3 ])
