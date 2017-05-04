# coding: utf-8
# проблема: найти подмассив, сделав xor на который мы получим максимальное число 1
# вход: строка из 0 и 1, например '010'
# выход: два индекса старт и финиш (счет начинается с 1)
# идея: каждый 0 добавляет 1, а один - вычитает, идя по массиву ищем макс. сумму,
# если сумма уходит в минус, игнорируем такой кусок, т.е. сдвигаем начальный индекс вправо

class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        m = 0
        s = 0
        left = 0
        inds = None
        for i in range(len(A)):
            s += 1 if A[i] == '0' else -1
            if s < 0:
                left = i + 1
                s = 0
            elif s > m:
                inds = [left + 1, i + 1]
                m = s
        if m <= 0:
            inds = []
        return inds

s = Solution()
print s.flip('010')
print s.flip('111')
print s.flip('1101')
print s.flip('0111000100010')
