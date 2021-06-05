
def topK(nums,k):
    freq = {}
    result = []
    for num in nums:
        freq[num] = freq.get(num,0)+1

    result = sorted(freq,key=freq.get,reverse=True)
    return result[:k]

nums = [1,1,1,2,2,3]
k = 2
print(topK(nums,k))

    

    