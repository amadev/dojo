class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        n = len(A)
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                break
        if i == n - 2:
            return [-1]
        for j in range(n - 1, 0, -1):
            if A[j] < A[j - 1]:
                break
        mn = min(A[i:j + 1])
        mx = max(A[i:j + 1])
        l = 0
        for l in range(0, i + 1):
            if A[l] > mn:
                break
        r = n - 1
        for r in range(n - 1, j - 1, -1):
            if A[r] < mx:
                break
        return [l, r]


s = Solution()
assert [-1] == s.subUnsort([1, 1, 1])
assert [-1] == s.subUnsort([1, 2, 3])
assert [0, 2] == s.subUnsort([3, 2, 1])
assert [1, 2] == s.subUnsort([1, 3, 2, 4, 5])
assert [0, 3] == s.subUnsort([1, 6, 0, 4])
