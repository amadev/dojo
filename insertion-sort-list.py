from linked_list import l2a, a2l, ListNode

def l2a(A):
    r = []
    while A is not None:
        r.append(A.val)
        A = A.next
    return r

def a2l(l):
    s = ListNode(l[0])
    A = s
    for i in range(1, len(l)):
        A.next = ListNode(l[i])
        A = A.next
    return s

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A is None or A.next is None:
            return A
        A = l2a(A)
        n = len(A)
        for i in range(1, n):
            j = i
            while j > 0 and A[j] < A[j - 1]:
                A[j], A[j - 1] = A[j - 1], A[j]
                j -= 1
        return a2l(A)


s = Solution()
assert [1] == l2a(s.insertionSortList(a2l([1])))
assert [1, 2, 3, 4, 5, 6] == l2a(s.insertionSortList(a2l([4, 3, 6, 5, 1, 2])))
