# coding: utf-8
# проблема: найти максимальный подмассив исключая отрицательные числа
# вход: массив
# выход: подмассив
# идея: модификация Kadane's algorithm, суммируем только положительные, при встрече отрицательного пропускаем его и сбрасываем промежуточную сумму

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        lm = [0, 0]
        tm = [0, 0]
        left = 0
        inds = None
        for i in range(len(A)):
            if A[i] >= 0:
                lm[0] += A[i]
                lm[1] += 1
                if lm > tm:
                    tm = lm[:]
                    inds = [left, i]
            else:
                lm = [0, 0]
                left = i + 1
        if not inds:
            return []
        return A[inds[0]:inds[1] + 1]



s = Solution()
print s.maxset([1, 2, 5, -7, 2, 3])
print s.maxset([ -1, -1, -1, -1, -1 ])
print s.maxset([ -846930886, -1714636915, 424238335, -1649760492 ])
