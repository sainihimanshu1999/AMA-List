'''
we make arrays of max of left and right, and then make an array of water, to store the water trapped at
a certain point
'''

def rain(height):
    n = len(height)
    left = [0]*n
    right = [0]*n
    water =[0]*n

    maxleft = 0
    maxright = 0

    for i in range(n):
        maxleft = max(maxleft,height[i])
        left[i] = maxleft
    for i in range(n-1,-1,-1):
        maxright = max(maxright,height[i])
        right[i] = maxright

    for i in range(n):
        water[i] = min(left[i],right[i]) - height[i]

    return sum(water)
        