
def reverse(head):
    if not head: return None

    prev = None
    curr = head
    while curr:
        new = curr.next
        curr.next= prev
        prev = curr
        curr= new
    head = prev
    return head