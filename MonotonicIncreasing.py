def monotonic(num):
    if num<10:
        return num

    A = list(str(num))
    i,length = 0,len(A)

    while i<length -1 and A[i]<=A[i+1]:
        i+=1
    
    if i==length:
        return num

    while i>0 and A[i]==A[i-1]:
        i-=1

    A[i] = str(int(A[i])-1)
    A[i+1:] = '9'*(length-i-1)

    return int(''.join(A))


print(monotonic(332))