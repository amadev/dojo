from linked_list import l2a, a2l, ListNode


class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        if A is None or B is None:
            return None
        s = ListNode(0)
        r = s
        while A is not None and B is not None:
            if A.val < B.val:
                c = A.val
                A = A.next
            else:
                c = B.val
                B = B.next
            r.next = ListNode(c)
            r = r.next
        if A is not None:
            while A is not None:
                r.next = ListNode(A.val)
                r = r.next
                A = A.next
        elif B is not None:
            while B is not None:
                r.next = ListNode(B.val)
                r = r.next
                B = B.next
        #print l2a(s)
        return s.next



s = Solution()
assert [1, 2, 3, 4] == l2a(s.mergeTwoLists(a2l([1, 3]), a2l([2, 4])))
assert [1, 2, 3, 4, 5, 6] == l2a(s.mergeTwoLists(a2l([1, 3, 5, 6]), a2l([2, 4])))
assert [1, 1, 2, 3] == l2a(s.mergeTwoLists(a2l([1]), a2l([1, 2, 3])))
