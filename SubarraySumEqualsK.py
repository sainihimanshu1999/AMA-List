'''
We are using dictionary to store the sums of subarray
'''

def sub(nums,k):
    dic = {}
    dic[0] = 1
    count,sumi =0,0

    for num in nums:
        sumi += num
        if sumi-k in dic:
            count += dic[sumi-k]

        if sumi in dic:
            dic[sumi] +=1
        else:
            dic[sumi] = 1

    return count

nums = [1,2,3]
print(sub(nums,3))