class Solution:
    # @param A : string
    # @return an integer
    def atoi(self, A):
        valid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        mx = (2**31 - 1)
        mn = - 2**31
        A = A.strip()
        n = len(A)
        if not n:
            return 0
        sign = 1
        if A[0] == '+':
            A = A[1:]
            n -= 1
        elif A[0] == '-':
            sign = -1
            A = A[1:]
            n -= 1
        if not n:
            return 0
        if A[0] not in valid:
            return 0
        i = 0
        for i in range(n):
            if A[i] != '0':
                break
        A = A[i:]
        n = len(A)
        if A[0] not in valid:
            return 0
        j = 0
        for i in range(n):
            if A[i] not in valid:
                break
            j += 1
            if i > 9:
                if sign == 1:
                    return mx
                return mn
        A = A[:j]
        if not A:
            return 0
        if int(A) > mx:
            if sign == 1:
                return mx
            return mn

        return int(A) * sign

s = Solution()
assert 0 == s.atoi('   ')
assert 1 == s.atoi('  1 ')
assert 1 == s.atoi('001')
assert 9 == s.atoi('+009')
assert -9 == s.atoi('-009')
assert 0 == s.atoi('++001')
assert 0 == s.atoi('+00a1')
assert 98 == s.atoi('0098a')
assert 2 ** 31 - 1 == s.atoi('11111111111')
assert -2 ** 31 == s.atoi('-11111111111')
assert 2 ** 31 - 1 == s.atoi('+0002147483649')
assert -2 ** 31 == s.atoi('-0002147483649')
