'''
In this question we are using basic mathematics
'''

def complex(s1,s2):
    digit1 = num1.split("+") 
    digit2 = num2.split("+") 

    digit1[1] = digit1[1].replace('i','') 
    digit2[1] = digit2[1].replace('i','') 

    first = (int(digit1[0])*int(digit2[0])) - (int(digit1[1])*int(digit2[1]))
    second = (int(digit1[0])*int(digit2[1])) + (int(digit1[0])*int(digit2[1]))

    return '{}+{}i'.format(first,second)


num1 = "1+1i"
num2 = "1+1i"

print(complex(num1,num2))
