class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a = map(int, A.split('.'))
        for i in range(len(a) - 1, -1, -1):
            if a[i] != 0:
                break

        a = a[:i+1]
        b = B.split('.')
        b[0] = b[0].lstrip('0')
        i = len(b) - 1
        for i in range(len(b) - 1, -1, -1):
            if b[i] != '0':
                break
        b = b[:i+1]
        a = map(int, a)
        b = map(int, b)
        return cmp(a, b)


s = Solution()
assert 0 == s.compareVersion('01', '1')
assert 0 == s.compareVersion('1.0', '1')
assert 1 == s.compareVersion('45555', '5.5')
