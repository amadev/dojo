
class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive = list(arrive)
        depart = list(depart)
        points = []
        for i in xrange(len(arrive)):
            points.append((arrive[i], 1))
            points.append((depart[i], 0))
        points.sort()
        x = 0
        for i in range(len(points)):
            if points[i][1]:
                x += 1
            else:
                x -= 1
            if x > K:
                return 0
        return 1


s = Solution()
assert 0 == s.hotel([1, 3, 5], [2, 6, 8], 1)
assert 1 == s.hotel([], [], 1)
assert 1 == s.hotel([10, 10], [10, 11], 1)
assert 1 == s.hotel([ 36, 45, 41, 7, 3, 44, 40, 46, 3, 16, 24, 3, 8, 33 ],
                    [ 71, 73, 85, 8, 11, 62, 64, 76, 25, 65, 25, 30, 36, 81 ],
                    14)
assert 1 == s.hotel([ 1, 2, 3 ],
                    [ 2, 3, 4 ],
                    1)
assert 1 == s.hotel(
    [ 9, 47, 17, 39, 35, 35, 20, 18, 15, 34, 11, 2, 45, 46, 15, 33, 47, 47, 10, 11, 27 ],
    [ 32, 82, 39, 86, 81, 58, 64, 53, 40, 76, 40, 46, 63, 88, 56, 52, 50, 72, 22, 19, 38 ],
    16)
assert 0 == s.hotel([ 1, 3, 4 ],
                    [12, 8, 6 ],
                    2)
assert 1 == s.hotel([ 40, 18 ],
                    [ 40, 43 ],
                    1)
