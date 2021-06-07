'''
In this question we have to add two number in linked list, which are in reversed order
'''

class ListNode:
    def __inti__(self,val=0,next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1,l2):
    dummy=curr=ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next

        if l2:
            carry += l2.val
            l2 = l2.next

        curr.next = ListNode(carry%10)
        curr = curr.next
        carry = carry//10
    return dummy.next