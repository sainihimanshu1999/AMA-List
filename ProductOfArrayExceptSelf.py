'''
product of any number xcept self in array can be calculated by findind the product of number in front + 
product of numbers in second
'''

def prod(nums):
    p = 1
    n = len(nums)
    result = []

    for i in range(n):
        result.append(p)
        p = p*nums[i]

    p =1

    for i in range(n-1,-1,-1):
        result[i] = result[i]*p
        p = p*nums[i]
    
    return result

nums = [1,2,3,4]
print(prod(nums))