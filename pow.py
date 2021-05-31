'''
Power functions without built in methods
'''

def power(x,n):
    if n== 0:
        return 1

    result = x
    increment = x

    for i in range(1,n):
        for i in range(1,x):
            result += increment
        increment = result

    return result


print(power(5,3))
