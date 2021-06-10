'''
Number of distinct subarrays with exact k elements is equal to subarrays with at most k elements - subarrays with at 
most k-1 elements
'''

from collections import Counter


def kdistinct(nums,k):
    return atmost(nums,k) - atmost(nums,k-1)

def atmost(nums,k):
    count = Counter()
    result = 0
    i = 0

    for j in range(len(nums)):
        if count[nums[j]]==0:
            k-=1
        count[nums[j]]+=1
        
        while k<0:  
            count[nums[i]]-=1
            if count[nums[i]]==0:
                k+=1
            i+=1
        result += j-i+1
    return result

nums = [1,2,1,2,3]
k = 2
print(kdistinct(nums,k))