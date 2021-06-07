'''
using simple method, O(logn)
'''
def check(n):
    if n == 0:
        return False

    while n>1:
        if(n%2!=0):
            return False
        n = n//2
    return True


'''
using bitwise operator O(1)
'''

def check2(n):
    if n ==0:
        return False
    
    elif n&(n-1) == 0:
        return True
    return False

#print(check2(32))


