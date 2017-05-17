# coding: utf-8
# name: merge sort
# description: |
#   рекурсивно разбиваем массив пополам, затем объединяем части, если
#   элемент из левой части больше - добавляем его, иначе из правой, не
#   забываем добавлять оставшуюся часть.


def merge(left, right):
    r = []
    while len(left) and len(right):
        if left[0] < right[0]:
            r.append(left.pop(0))
        else:
            r.append(right.pop(0))
    if len(left):
        r.extend(left)
    elif len(right):
        r.extend(right)
    return r


def mergesort(A):
    n = len(A)
    if n < 2:
        return A
    m = n / 2
    left = mergesort(A[0:m])
    right = mergesort(A[m:])
    return merge(left, right)

assert [1, 2, 3] == mergesort([3, 2, 1])
assert [1, 1, 1] == mergesort([1, 1, 1])
