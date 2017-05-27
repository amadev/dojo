class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        n = len(A)
        l = 0
        s = False
        for i in range(n - 1, -1, -1):
            if s and A[i] == ' ':
                break
            elif A[i] != ' ':
                l += 1
                s = True
        return l
        # A = A.strip()
        # if not A:
        #     return 0
        # return len(A.split()[-1])

s = Solution()
assert 0 == s.lengthOfLastWord('   ')
assert 3 == s.lengthOfLastWord('abc')
assert 1 == s.lengthOfLastWord('a b c')
