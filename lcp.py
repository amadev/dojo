class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        n = float('inf')
        for w in A:
            n = min(n, len(w))
        if n < 1:
            return ''
        p = ''
        for j in range(n):
            x = A[0][j]
            for i in range(1, len(A)):
                if A[i][j] != x:
                    return p
            p += x
        return p



s = Solution()
assert "a" == s.longestCommonPrefix([

  "abcdefgh",

  "aefghijk",

  "abcefgh"
])
assert "111" == s.longestCommonPrefix([
    "111",
    "111",
    "111"])

assert "" == s.longestCommonPrefix([

  "cabcdefgh",

  "aefghijk",

  "abcefgh"
])
