def count(n):
    ans = 0
    while n:
        ans += n%2
        n = n// 2
        #print(n)
    return ans

#print(count(5))


def count2(n):
    ans = 0
    while n:
        ans +=1
        n = n&(n-1)

    return ans

print(count2(6))


