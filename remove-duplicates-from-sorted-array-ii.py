class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if not n:
            return 0
        cnt = 1
        j = 1
        for i in range(n - 1):
            if A[i] == A[i + 1]:
                cnt += 1
                if cnt < 3:
                    A[j] = A[i + 1]
                    j += 1
            else:
                A[j] = A[i + 1]
                cnt = 1
                j += 1
        return j


s = Solution()
j = s.removeDuplicates([0, 0, 1, 1, 2, 2, 3, 3])

assert 0 == s.removeDuplicates([])
assert 2 == s.removeDuplicates([0, 0, 0])
assert 1 == s.removeDuplicates([1])
assert 3 == s.removeDuplicates([1, 1, 1, 2])
assert 2 == s.removeDuplicates([1, 1, 1, 1])
assert 4 == s.removeDuplicates([1, 1, 1, 1, 4, 4, 4])
assert 5 == s.removeDuplicates([1, 1, 1, 1, 4, 4, 5])
