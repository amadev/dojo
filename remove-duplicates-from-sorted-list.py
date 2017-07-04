# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        #print 'i', l2a(A)
        if A.next is None:
            return A
        s = A
        while A.next is not None:
            while A.val == A.next.val:
                A.next = A.next.next
                if A.next == None:
                    #print 'o', l2a(s)
                    return s
            A = A.next
        #print 'o', l2a(s)
        return s

s = Solution()

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


assert [1, 2] == l2a(s.deleteDuplicates(a2l([1, 1, 2, 2])))
assert [1] == l2a(s.deleteDuplicates(a2l([1, 1, 1])))
assert [1] == l2a(s.deleteDuplicates(a2l([1])))
assert [1, 2, 3, 4] == l2a(s.deleteDuplicates(a2l([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4])))
