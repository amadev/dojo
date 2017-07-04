from linked_list import l2a, a2l, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        n = 0
        h = A
        while A is not None:
            A = A.next
            n += 1
        B %= n
        if B == 0:
            return h
        A = h
        for i in range(n - B - 1):
            A = A.next
        nh = A.next
        A.next = None
        A = nh
        while A.next is not None:
            A = A.next
        A.next = h
        # print l2a(nh)
        return nh

# class Solution:
#     # @param A : head node of linked list
#     # @param B : integer
#     # @return the head node in the linked list
#     def rotateRight(self, A, B):
#         if A == None:
#             return None
#         temp = A
#         for i in xrange(B):
#             if temp.next == None:
#                 temp = A
#             else:
#                 temp = temp.next
#         last = A
#         while temp.next != None:
#             temp = temp.next
#             last = last.next
#         temp.next = A
#         res = last.next
#         last.next = None
#         return res

s = Solution()
assert [2, 1] == l2a(s.rotateRight(a2l([1, 2]), 1))
assert [3, 1, 2] == l2a(s.rotateRight(a2l([1, 2, 3]), 1))
assert [2, 3,  1] == l2a(s.rotateRight(a2l([1, 2, 3]), 2))
assert [1, 2, 3] == l2a(s.rotateRight(a2l([1, 2, 3]), 3))
assert [3, 1, 2] == l2a(s.rotateRight(a2l([1, 2, 3]), 4))
