'''
we will beusing monotonic queue method, Monotonic is a queue where numbers a arranged in decreasing order
from head to toe
'''
from collections import deque

def sliding(nums,k):
    q = deque()
    result = []

    for i,curr in enumerate(nums):
        while q and nums[q[0]]<=curr:
            q.pop()
        q.append(i)

        if q[0] == i-k:
            q.popleft()

        if i >= k-1:
            result.append(nums[q[0]])

    return result

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(sliding(nums,k))