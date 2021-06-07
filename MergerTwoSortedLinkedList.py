'''
There are two ways to do this question, one is interative and one is recursive, both have same time
complexity
'''

#iterative

def mergeTwoLists(l1,l2):
    dummy = curr = ListNode(0)
    while l1 or l2:
        if l1.val<l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1
    return dummy.next

#Recusrsive(feels less faster though)

def mergeTwoLists1(l1,l2):
    if not l1 or not l2:
        return l1 or l2
    
    if l1.val<l2.val:
        l1.next = mergeTwoLists1(l1.next,l2)
        return l1
    else:
        l2.next = mergeTwoLists1(l1,l2.next)
        return l2

    