A = [4, 3, 6, 5, 1, 2]
n = len(A)

for i in range(1, n):
    j = i
    while j > 0 and A[j] < A[j - 1]:
        t = A[j]
        A[j] = A[j - 1]
        A[j - 1] = t
        j -= 1

assert [1, 2, 3, 4, 5, 6] == A
