'''
when we have to divide linked list, we take two pointer approcah of slow and fast and then recurr in it,
it O(logn) time consuming
'''
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = None

def sortLinked(head):
    if not head or not head.next:
        return head

    slow,fast = head,head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    head2 = slow.next
    slow.next = None
    left = sortLinked(head)
    right = sortLinked(head2)
    return merge(left,right)

def merge(left,right):
    if not left or not right:
        return left or right

    dummy = curr = ListNode(None)

    while left and right:
        if left.val<right.val:
            curr.next = left
            left = left.next
        else:
            curr.next = right
            right = right.next
        curr = curr.next
    curr.next = left or right
    return dummy.next