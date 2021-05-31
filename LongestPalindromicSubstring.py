'''
We use bottom up dp approach in this, time complexity in O(n^2). we know that every element in diagonal 
is palindorm itself and we need to go below this diagonal because, it will lead to negative slicing which
is not valid
'''

def longestPalindrome(s):
    n = len(s)
    dp = [[False]*n for _ in range(n)]
    
    longestP = ''

    for i in range(n):
        dp[i][i] = True
        longestP = ''

    for i in range(n-1,-1,-1):
        for j in range(i+1,n):
            if s[i] == s[j]:
                if j-i == 1 and dp[i+1][j-1]:
                    dp[i][j] = True

                if len(longestP)<len(s[i:j+1]):
                    longestP = s[i:j+1]

    return longestP