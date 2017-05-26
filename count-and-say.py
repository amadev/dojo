class Solution:
    def calc(self, A):
        n = len(A)
        prev = None
        ind = 0
        cnt = {}
        for i in range(n):
            if prev is not None and prev != A[i]:
                ind += 1
            k = (ind, A[i])
            if k not in cnt:
                cnt[k] = 0
            cnt[k] += 1
            prev = A[i]
        r = ''
        for i in sorted(cnt.items()):
            r += str(i[1]) + i[0][1]
        return r

    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A < 1:
            return ''
        v = '1'
        for i in range(A - 1):
            v = self.calc(v)
        return v

s = Solution()
assert '' == s.countAndSay(0)
assert '1' == s.countAndSay(1)
assert '11' == s.countAndSay(2)
assert '111221' == s.countAndSay(5)
assert '212211' == s.calc('11221')
