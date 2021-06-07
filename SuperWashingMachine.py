'''
We have to count how many clothes we need in each machine to fulfill our need
'''

def washing(machine):
    total,n = sum(machine),len(machine)
    if total%n:
        return -1

    target,result,need = total//n,0,0

    for m in machine:
        need = m+need-target
        result = max(result,abs(need),m-target)

    return result


m = [1,0,5]
print(washing(m))

    