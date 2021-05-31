
#this have large time complexity, close to o(n^2) because of enumerate
def two(nums,target):
    dic = {}

    for i,num in enumerate(nums):
        rem = target-num
        if rem in dic:
            return [dic[rem],i]

        else:
            dic[num] = i


#this will have time complexity o(n)

def two1(nums,target):
    dic = {}
    i =0
    while i<len(nums):
        rem = target-nums[i]
        if rem in dic: 
            return [dic[rem],i]
        else:
            dic[nums[i]] = i

        i+=1


x = [2,8,9,3]
y = 10
print(two1(x,y))
