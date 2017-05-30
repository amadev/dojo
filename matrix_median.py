
# int median(vector<vector<int> > &A) {
#     int min = A[0][0], max = A[0][0];
#     int n = A.size(), m = A[0].size();
#     for (int i = 0; i < n; ++i) {
#         if (A[i][0] < min) min = A[i][0];
#         if (A[i][m-1] > max) max = A[i][m-1];
#     }

#     int element = (n * m + 1) / 2;
#     while (min < max) {
#         int mid = min + (max - min) / 2;
#         int cnt = 0;
#         for (int i = 0; i < n; ++i)
#             cnt += upper_bound(&A[i][0], &A[i][m], mid) - &A[i][0];
#         if (cnt < element)
#             min = mid + 1;
#         else
#             max = mid;
#     }
#     return min;
# }

class Solution:
    # @param A : list of list of integers
    # @return an integer

    def lessthan(self, A, x):
        n = len(A)
        i = 0
        while i < n and x >= A[i]:
            i += 1
        return i

    def findMedian(self, A):
        if not A:
            return
        n = len(A)
        m = len(A[0])
        mn = float("inf")
        mx = -float("inf")
        for i in range(n):
            mn = min(mn, A[i][0])
            mx = max(mx, A[i][-1])
        e = (n * m + 1) / 2
        while mn < mx:
            cnt = 0
            m = mn + (mx - mn) / 2
            for i in range(n):
                cnt += self.lessthan(A[i], m)
            if cnt < e:
                mn = m + 1
            else:
                mx = m
        return mn


s = Solution()
assert 5 == s.findMedian([[1, 3, 5], [2, 6, 9], [3, 6, 9]])
#print s.lessthan([1, 2, 3], 5)
