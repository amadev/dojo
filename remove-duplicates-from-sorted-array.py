class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if not n:
            return 0
        j = 1
        for i in range(n - 1):
            if A[i] != A[i + 1]:
                A[j] = A[i + 1]
                j += 1
        return j


s = Solution()
assert 0 == s.removeDuplicates([])
assert 1 == s.removeDuplicates([0, 0])
assert 3 == s.removeDuplicates([1, 2, 3])
assert 1 == s.removeDuplicates([1, 1])
assert 2 == s.removeDuplicates([1, 1, 2])
assert 4 == s.removeDuplicates([1, 1, 1, 2, 2, 3, 3, 3, 4])
