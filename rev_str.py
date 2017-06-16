class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        A = A.strip()
        return ' '.join(reversed(A.split()))


s = Solution()
assert 'c b a' == s.reverseWords('a b c')
assert '' == s.reverseWords('')
assert 'a' == s.reverseWords('a')
