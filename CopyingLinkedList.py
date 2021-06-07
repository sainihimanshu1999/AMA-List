'''
we have to create deep copy of linked list(which is basically having same list with there own node),
this question specifically has random pointer, otherwise it can be used to deep copy simple list also
'''

def deepCopy(head):
    if not head: 
        return None

    maps = {}
    curr = head
    while curr:
        maps[curr] = Node(curr.val,None,None)
        curr = curr.next

    curr = head
    while curr:
        if curr.next:
            maps[curr].next = maps[curr.next]
        if curr.random:
            maps[curr].random = maps[curr.random]

        curr = curr.next

    return maps[head]