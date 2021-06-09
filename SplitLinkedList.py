'''
Counting the length of linked list and then calculating the chunks of needed to divide it
'''

def split(head,k):
    curr,length = head,0
    while curr:
        curr = curr.next
        length +=1

    chunk_size,longest = length//k, length%k

    result= [chunk_size+1]*longest + [chunk_size]*longest
    prev,curr = None,head

    for index,num in enumerate(result):
        if prev: prev.next = None

        result[index] = curr
        for i in range(num):
            prev,curr = curr,curr.next

    return result
    