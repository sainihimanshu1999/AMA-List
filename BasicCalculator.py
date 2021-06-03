'''
In this question the we have to perform basic calcultor fucntion without using built in methods
'''

def calci(s):
    result,num,sign,stack = 0,0,1,[]

    for dig in s:
        if dig.isdigit():
            num = num*10+ int(dig)

        elif dig in ['+','-']:
            result += sign*num
            num = 0
            sign = 1 if dig =='+' else -1
        
        elif dig =='(':
            stack.append(result)
            stack.append(sign)
            result,sign =0,1

        elif dig ==')':
            result += sign*num
            result *= stack.pop()
            result += stack.pop()
            num = 0
    return result + sign*num


s = "(1+(4+5+2)-3)+(6+8)"
print(calci(s))


