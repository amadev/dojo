# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        e = []
        for i in intervals:
            e.append((i[0], 0))
            e.append((i[1], 1))
        e.append((new_interval[0], 0))
        e.append((new_interval[1], 1))
        e.sort()
        cnt = 0
        r = []
        for i in e:
            if cnt == 0:
                s = i[0]
            if i[1] == 0:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                r.append([s, i[0]])
        return r


s = Solution()
assert [[1, 5], [6, 9]] == s.insert([[1, 3], [6, 9]], [2, 5])
