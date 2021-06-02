'''
This question is more space oriented question it can be done by two methods
'''

#matrix method O(m*m) space

def pascal(num):
    dp = [[1]*(num+1) for _ in range(num+1)]

    for i in range(num+1):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]

    return dp[-1]


#table method O(m) space

def pascal2(num):
    dp = [1]*(num+1)

    for i in range(2,num+1):
        for j in range(i-1,0,-1):
            dp[j] += dp[j-1]

    return dp


print(pascal2(7))