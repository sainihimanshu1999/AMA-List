def cycle(head):
    maps = {}
    curr = head
    while curr:
        if curr in maps:
            return True
        maps[curr] = curr
        curr = curr.next

    return False