'''
we have to convert this string to integer without using inbuilt functions
'''

def atoi(s):
    s = s.strip()

    if not s: return 0
    result = 0

    negative = False

    if s[0] == '-':
        negative = True
    
    elif not s[0].isnumeric():
        return 0
    
    elif s[0].isnumeric():
        result = ord(s[0])-ord('0')

    for i in range(1,len(s)):
        if s[i].isnumeric():
            result = result*10 + (ord(s[i])-ord('0'))

            if negative  and result>=2147483648:
                return -2147483648
            if not negative and result>=2147483648:
                return 2147483647
        else: break
        
    
    if negative:
        return -result
    return result


s = '-2147483650'
print(atoi(s))

