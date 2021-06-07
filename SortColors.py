'''
The algoritm used is dutch partioning algorithm, it is inspired by the flag of netherland
'''

def colors(nums):
    red,white,blue = 0,0,len(nums)-1

    while white<=blue:
        if nums[white] == 0:
            nums[red],nums[white] = nums[white],nums[red]
            white+=1
            red+=1
        elif nums[white] ==1:
            white +=1
        else:
            nums[blue],nums[white] = nums[white],nums[blue]
            blue -=1

    return nums

print(colors([1,0,1,2,1]))

