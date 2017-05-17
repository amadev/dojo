# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) < 2:
            return intervals
        e = []
        for i in intervals:
            e.append((i[0], 0))
            e.append((i[1], 1))
        e.sort()
        cnt = 0
        r = []
        for i in e:
            if cnt == 0:
                st = i[0]
            if i[1] == 0:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                r.append([st, i[0]])

        return r

s = Solution()
# assert [[1,6],[8,10],[15,18]] == s.merge([[1,3],[2,6],[8,10],[15,18]])
# assert [[1, 1]] == s.merge([[1,1],[1,1]])
# assert [[1, 2],[3, 4]] == s.merge([[1,2],[3,4]])
assert [[1, 10]] == s.merge([ (1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 6) ])
