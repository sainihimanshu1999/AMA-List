'''
This solution have O(n^2) even having 3 loops for the 3rd loop maybe run when there is a need to check
'''

def three_sum(nums):
    n= len(nums)
    nums.sort()
    result = []

    for i in range(n-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = n-1

        while left<right:
            total = nums[i]+nums[left]+nums[right]

            if total<0:
                left+=1
            elif total>0:
                right -=1
            else:
                result.append([nums[i],nums[left],nums[right]])

                while left<right and nums[left] == nums[left+1]:
                    left+=1
                while left<right and nums[right] == nums[right-1]:
                    right -=1

                left +=1
                right-=1
    return result


a = [-1,0,1,2,-1,-4]
print(three_sum(a))