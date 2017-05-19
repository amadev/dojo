class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        fl = []
        st = True
        for i in range(len(A)):
            if A[i] == 0 and st:
                continue
            else:
                st = False
                fl.append(A[i])
        A = fl
        if len(A) == 0:
            return [1]
        for i in range(len(A) - 1, -1, -1):
            if A[i] < 9:
                A[i] += 1
                break
            else:
                A[i] = 0
                if i == 0:
                    A.insert(0, 1)
                    break
        return A


s = Solution()
print s.plusOne([ 0, 0, 4, 4, 6, 0, 9, 6, 5, 1 ])

# assert [1] == add_one([])
# assert [2] == add_one([1])
# assert [2, 0] == add_one([0, 1, 9])
# assert [1, 0, 0, 0] == add_one([9, 9, 9]), add_one([9, 9, 9])




# def add_one(A):
#         A = filter(lambda x: x != 0, A)
#         if len(A) == 0:
#             return [1]
#         for i in range(len(A) - 1, -1, -1):
#             print i, A[i]
#             if A[i] < 9:
#                 A[i] += 1
#                 break
#             else:
#                 A[i] = 0
#                 if i == 0:
#                     A.insert(0, 1)
#                     break
#         return A


# assert [1] == add_one([])
# assert [2] == add_one([1])
# assert [2, 0] == add_one([0, 1, 9])
# assert [1, 0, 0, 0] == add_one([9, 9, 9]), add_one([9, 9, 9])

# print add_one([ 2, 5, 6, 8, 6, 1, 2, 4, 5 ])
