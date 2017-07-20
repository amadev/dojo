class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def naive(self, A, B):
        n = len(A)
        d = float('inf')
        s = None
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    ns = A[i] + A[j] + A[k]
                    nd = min(d, abs(B - ns))
                    if nd != d:
                        s = ns
                    d = nd
        return s

    def threeSumClosest(self, A, B):
        n = len(A)
        if n < 3:
            return
        A = list(A)
        A.sort()
        #print '=', A
        mn = float('inf')
        r = None
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                s = A[i] + A[j] + A[k]
                #print 'A[i], A[j], A[k], s',  A[i], A[j], A[k], s
                diff = abs(s - B)
                if diff < mn:
                    mn = diff
                    r = s
                if diff == 0:
                    return B
                if s <= B:
                    j += 1
                else:
                    k -= 1
        #print 'r', r
        return r

s = Solution()

assert None == s.threeSumClosest([-1, 2], 1)
assert 4 == s.threeSumClosest([-1, 2, 3], 100)
assert 2 == s.threeSumClosest([-1, 2, 1, -4], 1)
assert -1 == s.threeSumClosest([ -5, 1, 4, -7, 10, -7, 0, 7, 3, 0, -2, -5, -3, -6, 4, -7, -8, 0, 4, 9, 4, 1, -8, -6, -6, 0, -9, 5, 3, -9, -5, -9, 6, 3, 8, -10, 1, -2, 2, 1, -9, 2, -3, 9, 9, -10, 0, -9, -2, 7, 0, -4, -3, 1, 6, -3 ], -1)

assert -1 == s.threeSumClosest([-7, -6, -2, -1, 6, 7, 8], -1)
assert 5 == s.threeSumClosest([ 5, -2, -1, -10, 10 ], 5)
