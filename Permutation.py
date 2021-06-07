'''
we use dfs in this method becuase it will give all the possibilities of permutations
'''

def permutation(nums):
    result = []
    dfs(nums,[],result)
    return result


def dfs(nums,path,result):
    if not nums:
        result.append(path)
    for i in range(len(nums)):
        dfs(nums[:i]+nums[i+1:],path+[nums[i]],result)



print(permutation([1,2,3]))