# 0, 0
# 1, 0; 0, 1
# 2, 0; 1, 1; 0, 2
# 1, 2; 2, 1
# 2, 2

class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
            r = []
            n = len(a)
            for k in range(2 * n - 1):
                row = []
                if k < n:
                    i = 0
                    j = k
                    while i < k + 1:
                        row.append(a[i][j])
                        i += 1
                        j -= 1
                else:
                    i = k - n + 1
                    j = n - 1
                    while i < n:
                        row.append(a[i][j])
                        i += 1
                        j -= 1
                r.append(row)
            return r


s = Solution()
# print s.diagonal([])
# print s.diagonal([[1, 2], [3, 4]])
print s.diagonal([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
