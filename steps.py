def distance(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    if x > y:
        return x
    else:
        return y



A = [(0, 0), (1, 1), (1, 2)]


print(sum(distance(A[i], A[i+1]) for i in range(len(A) - 1)))





print distance([0,0], [0,5])
print distance([0,0], [2,3])
