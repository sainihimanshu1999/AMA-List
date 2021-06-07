'''
In this question we are using dynamic programming, dp[i][j] means edit distance till word1[:i] and word2[:j]

'''

def editDistance(word1,word2):
    m = len(word1)
    n = len(word2)

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i

    for i in range(n+1):
        dp[0][i] = i

    for i in range(1,m+1):
        for j in range(1,n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])

    return dp[-1][-1]


print(editDistance('horse','ros')) 
