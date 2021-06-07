'''
We use dictionary, to calculate the frequency and then check the pairs
'''

from collections import Counter

def kdiff(nums,k):
    freq = Counter(nums)
    count = 0
    if k>0:
        count = sum(i+k in freq for i in freq)
    else:
        count = sum(freq[i]>1 for i in freq)

    return count

nums = [3,1,4,1,5]
k = 2
print(kdiff(nums,k))
