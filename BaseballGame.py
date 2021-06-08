def calPoints(ops):
    stack = []
    
    for op in ops:
        if op == 'C':
            stack.pop()
        elif op =='D':
            x = 2*stack[-1]
            stack.append(x)
        elif op == '+':
            a = stack[-1]
            b = stack[-2]
            stack.append(a+b)
        else:
            stack.append(int(op))
            
    return sum(stack)

