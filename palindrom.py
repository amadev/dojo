class Solution:
    # @param A : integer
    # @return a boolean value ( True / False )
    def isPalindrome(self, A):
        if A < 0:
            return False
        A = str(A)
        n = len(A)
        for i in range(n / 2):
            if A[i] != A[n - i - 1]:
                return False
        return True

s = Solution()
print s.isPalindrome(12121)
print s.isPalindrome(-1)
print s.isPalindrome(0)
print s.isPalindrome(11)
