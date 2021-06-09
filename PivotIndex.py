'''
This question have many solutions but we use enumeate solution to optimize the solution
'''

def pivot(nums):
    sumi = sum(nums)
    lsumi = 0

    for i, num in enumerate(nums):
        rsumi = sumi-lsumi-num
        if rsumi == lsumi:
            return i
            break
        lsumi +=num
    return -1


a = [1,7,3,6,6,5]
print(pivot(a))