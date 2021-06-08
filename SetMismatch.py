'''
There are two ways of tackling this problem, on is by using arrays and other is just by using elementary maths
'''

#array method

def errornumber(nums):
    n = len(nums)
    count = [0]*(n+1)

    for num in nums:
        count[num]+=1

    for i in range(n+1):
        if count[i]==2:
            twice = i
        if count[i]==0:
            never = i

    return [twice,never]


#elementary maths

def error2(nums):
    n = len(nums)
    A = n*(n+1)//2 - sum(nums)
    B = n*(n+1)*(2*n+1)//6 - sum(num*num for num in nums)
    return [(B-A*A)//2//A, (B+A*A)//2//A]
print(error2([2,2]))