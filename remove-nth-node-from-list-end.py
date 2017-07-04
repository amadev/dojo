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
    def removeNthFromEnd(self, A, B):
        n = 0
        head = A
        while A is not None:
            A = A.next
            n += 1
        A = head
        if not n or B < 1:
            return
        if n - B <= 0:
            return A.next
        for i in range(n - B - 1):
            A = A.next
        A.next = A.next.next
        #print l2a(head)
        return head



s = Solution()
assert [1, 2, 3, 5] == l2a(s.removeNthFromEnd(a2l([1, 2, 3, 4, 5]), 2))
assert [1, 2, 3, 4] == l2a(s.removeNthFromEnd(a2l([1, 2, 3, 4, 5]), 1))
assert [ 2, 3, 4, 5] == l2a(s.removeNthFromEnd(a2l([1, 2, 3, 4, 5]), 5))
assert [ 2, 3, 4, 5] == l2a(s.removeNthFromEnd(a2l([1, 2, 3, 4, 5]), 6))
