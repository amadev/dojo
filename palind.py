class Solution:

    def is_alnum(self, x):
        o = ord(x)
        if o >= ord('1') and o <= ord('9'):
            return True
        if o >= ord('a') and o <= ord('z'):
            return True
        return False
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = A.lower()
        A = filter(self.is_alnum, A)
        n = len(A)
        for i in range(n / 2):
            if A[i] != A[n-i-1]:
                return 0
        return 1

s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
#assert "A man, a plan, a canal: Panama" ==
