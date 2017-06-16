# coding: utf-8
# найти дублирующийся и недостающий элемент

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        dup = None
        i = 0
        while i < len(A):
            if A[i] == i + 1:
                i += 1
            else:
                tind = A[i] - 1
                if A[tind] == tind + 1:
                    dup = A[i]
                    break
                tmp = A[tind]
                A[tind] = A[i]
                A[i] = tmp
        if dup:
            t = sum(A) - dup
            return dup, sum(xrange(len(A) + 1)) - t
        return None

s = Solution()
print s.repeatedNumber([3, 1, 2, 5, 3])
print s.repeatedNumber([3, 1, 5, 4, 5])
print s.repeatedNumber([]).
