# Дано:
# - набор книг с указанием количества страниц:
#   [60, 231, 514] - книга 1 - 60 стр., книга 2 - 231 стр и т.д.
# - количество студентов

# Нужно:
#   найти минимальное количество страниц, которые должен прочитать один студент.
#   Для 3 студентов это 60, для 2-х 291.

# Решение:
#   Методом binary search ищем количество страниц, которое разбивается
#   на нужное кол-во студентов.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def books(self, A, B):
        if len(A) < B:
            return -1
        lo = min(A)
        hi = sum(A)
        while lo < hi:
            print("Maxmin: ", lo, hi)
            mid = (lo + hi) // 2
            num_students = self.number_of_students_required(A, mid)
            print('!num_students', type(num_students), num_students)
            if num_students == -1:
                lo = mid + 1
            elif num_students < B:
                hi = mid
            else:
                lo = mid + 1
        return lo


    def number_of_students_required(self, books, pages_per_student):
        num_students = 0
        num_pages = 0
        # import ipdb; ipdb.set_trace()
        for pages in books:
            if pages > pages_per_student:
                return -1
            num_pages += pages
            if num_pages > pages_per_student:
                num_students += 1
                num_pages = pages
        return num_students


s = Solution()
assert 5 == s.books([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2)
# assert 3 == s.books([1, 2, 3], 2)
# assert 9 == s.books([1, 2, 3, 4, 5, 6], 3)
# assert 113 == s.books([ 12, 34, 67, 90 ], 2)
# assert 110 == s.books([ 73, 58, 30, 72, 44, 78, 23, 9 ], 5)
