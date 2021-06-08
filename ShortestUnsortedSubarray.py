'''
In this question we have to find the shortest unsorted sub array that if sorted will sort the whole subarray
'''

def short(nums):
    sorted_nums = sorted(nums)
    start = 0
    end = len(nums)-1

    if sorted_nums == nums:
        return 0

    while sorted_nums[start] == nums[start]:
        start +=1

    while sorted_nums[end] == nums[end]:
        end -=1

    return end-start+1


nums = [2,6,4,8,10,9,15]
print(short(nums))