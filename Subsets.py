'''
In this question we are using basic dfs, because one can visualize it as a tree
power set is the set which contains all  the subsets including null and set itself
'''

def subsets(nums):
    result = []
    dfs(sorted(nums),[],result)
    return result

def dfs(nums,path,result):
    result.append(path)

    for i in range(len(nums)):
        dfs(nums[i+1:],path+[nums[i]],result)


num = [1,2,3,4]
print(subsets(num))