from linked_list import l2a, a2l, ListNode


class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reverseList(self, A):

        prev = None
        current = A
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev


s = Solution()
assert [4, 3, 2, 1] == l2a(s.reverseList(a2l([1, 2, 3, 4])))
assert [1] == l2a(s.reverseList(a2l([1])))
