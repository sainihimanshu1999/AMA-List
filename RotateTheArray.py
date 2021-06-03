'''
This question is suppposed to be done in O(1) space, the first approach is cyclic replacement algorithm
'''

#cyclic replacement algorithm

def rotate(nums,k):
    n = len(nums)
    k = k%n

    start=count = 0
    while count<n:
        curr,prev = start,nums[start]
        while True:
            next_index = (curr+k)%n
            nums[next_index],prev = prev,nums[next_index]
            curr = next_index
            count +=1

            if start == curr:
                break

        start +=1
    return nums


nums = [1,2,3,4,5,6,7]
print(rotate(nums,3))

