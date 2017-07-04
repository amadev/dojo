class Solution:
    def naive(self, A):
        A.sort()
        n = len(A)
        r = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if A[i] + A[j] > A[k]:
                        # # print '-', A[i], A[j], A[k]
                        r += 1
        return r

    def cnt_k(self, A, k):
        i = k - 1
        r = 0
        while i > 0:
            j = i - 1
            while j >= 0:
                # print 'k, i, j', k, i, j
                # print A[i], A[j], A[k]
                if A[i] + A[j] > A[k]:
                    r += 1
                    # print 'add result', r
                else:
                    break
                j -= 1
            i -= 1
        return r


    # @param A : list of integers
    # @return an integer
    def f1(self, A):
        n = len(A)
        if n < 3:
            return 0
        A.sort()
        # print 's', A
        r = 0
        k = 2
        while k < n:
            r += self.cnt_k(A, k)
            k += 1
        return r

    def nTriang(self, A):
        n = len(A)
        A.sort()
        r = 0
        for i in range(0,n-2):
            k = i + 2
            for j in range(i+1,n):
                while (k < n and A[i] + A[j] > A[k]):
                    k += 1
                r += k - j - 1
        return r % (1e9 + 7)



s = Solution()
assert 4 == s.nTriang([1, 1, 1, 2, 2])
assert 12 == s.nTriang([ 4, 6, 13, 16, 20, 3, 1, 12 ])

# - 3 4 6
# - 3 12 13
# - 4 12 13
# - 4 13 16
# - 6 12 13
# - 6 12 16
# - 6 13 16
# - 6 16 20
# - 12 13 16
# - 12 13 20
# - 12 16 20
# - 13 16 20
