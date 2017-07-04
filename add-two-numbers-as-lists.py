from linked_list import l2a, a2l, ListNode

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        a, b = A, B
        head = ListNode(0)
        cur_sum = head
        while a != None or b != None or cur_sum.val > 9:
            carry = cur_sum.val / 10
            cur_sum.val %= 10
            a_val = 0 if a == None else a.val
            b_val = 0 if b == None else b.val
            next_val = a_val + b_val + carry
            cur_sum.next = ListNode(next_val)
            cur_sum = cur_sum.next
            a = None if a == None else a.next
            b = None if b == None else b.next
        return head.next

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        r = ListNode(0)
        head = r
        rem = 0
        while A is not None or B is not None:
            a = 0
            if A:
                a = A.val
            b = 0
            if B:
                b = B.val
            v = a + b + rem
            rem = 0
            if v > 9:
                rem = 1
                v = int(str(v)[1])
            r.next = ListNode(v)
            r = r.next
            if A:
                A = A.next
            if B:
                B = B.next
        if rem:
            r.next = ListNode(rem)
        r = head.next
        cnt = 0
        n = 0
        while r is not None:
            if r.val == 0:
                cnt += 1
            else:
                cnt = 0
            n += 1
            r = r.next
        # print n, cnt
        r = head.next
        if cnt:
            for i in range(n - cnt - 1):
                r = r.next
            r.next = None
        # print l2a(head.next)
        return head.next

s = Solution()
assert [2] == l2a(s.addTwoNumbers(a2l([1]), a2l([1])))
assert [3, 3, 1] == l2a(s.addTwoNumbers(a2l([3, 3]), a2l([0, 0, 1])))
assert [3, 3, 1] == l2a(s.addTwoNumbers(a2l([3, 3]), a2l([0, 0, 1, 0])))
assert [0, 0, 1, 1] == l2a(s.addTwoNumbers(a2l([9, 9, 5, 0, 0]), a2l([1, 0, 5, 0])))
