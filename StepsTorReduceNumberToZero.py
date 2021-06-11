'''
Using bit wise operators
'''

def reduce(num):
    count = 0
    while num:
        num = num -1 if num&1 else num>>1
        count +=1
    return count


print(reduce(14))