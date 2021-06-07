'''
In this question we have use divide and conquer algorithm, in divide and conquer we make parts of input
according to the constraints given and then solve them one by one to solve our question
'''

class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def mergeLists(lists):

    if not lists:
        return []

    if len(lists) == 1:
        return lists[0]

    mid = len(lists)//2

    left,right = mergeLists(lists[:mid]),mergeLists(lists[mid:])

    return merge(left,right)

def merge(l1,l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val<l2.val:
            curr.next = l1
            l1 = l1.next

        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

