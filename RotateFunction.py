
def maxRotate(nums):
    arrSum = sum(nums)
    sumProduct = 0

    for i,val in enumerate(nums):
        sumProduct += i*val

    n = len(nums)
    max_value = sumProduct

    for i in range(1,n):
        sumProduct += (arrSum -nums([-i]*n))
        max_value = max(max_value,sumProduct)

    return max_value