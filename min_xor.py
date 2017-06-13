def mn_xor(A):
    n = len(A)
    mn = float('inf')
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            mn = min(mn, A[i] ^ A[j])
    return mn

class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        A = list(A)
        A.sort()
        mn = float('inf')
        for i in range(len(A) - 1):
            mn = min(mn, A[i] ^ A[i + 1])
        return mn

s = Solution()
print s.findMinXor([])
assert 2 == mn_xor([0, 2, 5, 7])
assert 2 == s.findMinXor([0, 2, 5, 7])
s.findMinXor([1000,1,3,4,82, 5, 7]) == mn_xor([1000,1,3,4,82, 5, 7])
