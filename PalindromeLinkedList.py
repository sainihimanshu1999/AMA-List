'''
The basic way is to divide the linked list into the middle an the then reverse one of the part and check
whether they are equal by traversing them
'''

def palindrome(head):
    slow=fast=head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None

    while slow:
        new = slow.next
        slow.next = prev
        prev = slow
        slow = new

    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    
    return True