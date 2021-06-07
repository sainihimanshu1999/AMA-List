'''
Count prime can be silved using seive algorithm
'''

#brute Force

def prime(n):
    count = 0
    for num in range(n):
        if num>1:
            for j in range(2,num):
                if num%j==0:
                    break
            else:
                count+=1

    return count

#sieve method

def prime2(n):
    if n<3: return 0

    arr =[1]*n
    arr[0]=arr[1] = 0

    m=2
    while m*m<n:
        if arr[m] == 1:
            
            for i in range(m*m,n,m):
                arr[i] = 0

        m += 1 if m==2 else 2
    return sum(arr)

#sieve optimized

def prime3(n):
    if n<3:
        return 0

    arr = [1]*n
    arr[0]=arr[1] =0

    m=2
    while m*m<n:
        if arr[m]==1:
            arr[m*m:n:m] = [0]*(1+(n-m*m-1)//m)

        m += 1 if m==2 else 2
    return sum(arr)
print(prime3(1000))
