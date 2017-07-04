class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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
