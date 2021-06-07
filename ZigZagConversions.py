'''
This question was rally not about zig zag pattern it's more about adding every element of string into the
next row
'''

def zigZag(s,k):
    n = len(s)
    if k == 1 or k>n:
        return s

    rows = ['']*k
    index = 0
    step = 1

    for x in s:
        rows[index] += x  

        if index == 0:
            step = 1
        elif index  == k-1:
            step = -1

        index += step

    return ''.join(rows) 


s = 'PAYPALISHIRING'
k = 3

print(zigZag(s,k))
