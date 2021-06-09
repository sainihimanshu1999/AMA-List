'''
Minimum cost of climbing stairs, either two steps or one
'''

def minCost(cost):
    cost.append(0)
    n = len(cost)


    dp = [0]*(n+1)
    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2,n):
        dp[i] = cost[i]+min(dp[i-1],dp[i-2])
    return dp[-1]

