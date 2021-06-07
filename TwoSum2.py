'''
here the list is already sorted and we can't repeat the numbers
'''

def twoSum(nums,target):
    left = 0
    right = len(nums)-1

    while left<right:
        if nums[left]+nums[right] == target:
            return[left+1,right+1]
        elif nums[left]+nums[right]<target:
            left+=1
        else:
            right -=1