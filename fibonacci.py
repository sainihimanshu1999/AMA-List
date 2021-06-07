def fib(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


def fib2(n):
    arr = [0,1]

    for i in range(2,n+1):
        ans = arr[i-1]+arr[i-2]
        arr.append(ans)

    return arr[n]

print(fib2(1000))