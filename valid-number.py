
nums = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
signs = {'+', '-'}
valid = nums | signs | {'.'} | {'e'}

class Solution:
    def check_float(self, x):
        if not x:
            return 0
        for i in range(len(x)):
            if x[i] not in nums | signs | {'.'}:
                return 0
        if x[0] in signs:
            x = x[1:]
        if not x:
            return 0
        for i in range(len(x)):
            if x[i] not in nums | {'.'}:
                return 0
        p = x.find('.')
        if p != -1:
            if p == len(x) - 1:
                return 0
            if x[p + 1] not in nums:
                return 0
        return 1

    def check_int(self, x):
        if not x:
            return 0
        for i in range(len(x)):
            if x[i] not in nums | signs:
                return 0
        if x[0] in signs:
            x = x[1:]
        if not x:
            return 0
        for i in range(len(x)):
            if x[i] not in nums:
                return 0
        return 1

    # @param A : string
    # @return an integer
    def isNumber(self, A):
        A = A.strip()
        if not A:
            return 0
        for i in range(len(A)):
            if A[i] not in valid:
                return 0
        p = A.split('e')
        if len(p) > 2:
            return 0
        if not self.check_float(p[0]):
            return 0
        if len(p) == 2:
            if not self.check_int(p[1]):
                return 0
        return 1


s = Solution()
assert 0 == s.isNumber('')
assert 1 == s.isNumber('000')
assert 1 == s.isNumber('001')
assert 1 == s.isNumber('1e5')
assert 0 == s.isNumber('1-2')
assert 1 == s.isNumber('-0.1e-10')
assert 0 == s.isNumber('-0.1e-1e-0')
assert 0 == s.isNumber('-eee')
assert 0 == s.isNumber('eee')
assert 0 == s.isNumber('3.')
assert 0 == s.isNumber('3+')
assert 0 == s.isNumber('-e-1')
assert 0 == s.isNumber('+  ')
assert 0 == s.isNumber('.e-10')
assert 1 == s.isNumber('.1e-10')
assert 0 == s.isNumber('-.e-10')
assert 1 == s.isNumber('-.1e-10')
assert 0 == s.isNumber('3e1.1')
assert 0 == s.isNumber('1.e1')
assert 0 == s.isNumber('1e')
