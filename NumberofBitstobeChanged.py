'''
ways to convert normal number into binary
'''
# def db(num):
     
#     if num >= 1:
#         db(num // 2)
#     print(num % 2, end = '')


# #using builtin function

# def db2(n):
#     return bin(n).replace('0b','')

'''
Solution
'''

def convert(a,b):
    n = a^b
    count = 0

    while n:
        count +=1
        n = n&(n-1)

    return(count)

print(convert(1,8))
