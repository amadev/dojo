class Solution:
    # @param haystack : string
    # @param needle : string
    # @return an integer
    def strStr(self, haystack, needle):
        if not haystack or not needle:
            return -1
        if haystack == needle:
            return 0
        n = len(haystack)
        m = len(needle)
        j = 0
        i = 0
        while i < n:
            if not j and haystack[i] == needle[0]:
                j = 1
                i += 1
                continue
            if j:
                if haystack[i] != needle[j]:
                    i = i - j
                    j = 0
                else:
                    j += 1
            if j == m:
                return i + 1 - m
            i += 1
        return -1

s = Solution()
assert -1 == s.strStr('', 'abc')
assert -1 == s.strStr('dsa', '')
assert -1 == s.strStr('', '')

assert 0 == s.strStr('a', 'a')

assert 0 == s.strStr('abcde', 'abc')
assert 3 == s.strStr('xxxabcde', 'abc')
assert -1 == s.strStr('xab', 'abc')
assert 3 == s.strStr('xxxabc', 'abc')
assert 2 == s.strStr('ababc', 'abc')
assert 48 == s.strStr("bbaabbbbbaabbaabbbbbbabbbabaabbbabbabbbbababbbabbabaaababbbaabaaaba", "babaaa")
assert 13 == s.strStr("aabaaaababaabbbabbabbbaabababaaaaaababaaabbabbabbabbaaaabbbbbbaabbabbbbbabababbaaabbaabbbababbb", "bba")
