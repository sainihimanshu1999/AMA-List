
def intersect(head1,head2):
    if not head1 or not head2:
        return None
    
    pA = head1
    pB = head2

    while pA!=pB:
        pA = pA.next if pA else head2
        pB = pB.next if pB else head1

    return pA