'''
We use dp memoization in this question and easily count the score at each interval the max score we can achive if we 
start from  some particular point
'''

def stoneGame(values):
    memo  = {}

    def dfs(start):
        if start >= len(values):
            return 0
        
        if start in memo:
            return memo[start]

        memo[start] =  float('-inf')
        score = 0

        for i in range(start,min(start+3,len(values))):
            score += values[i]
            memo[start] = max(memo[start],score-dfs(i+1))

        return memo[start]

    score = dfs(0)
    return 'Tie' if score ==0 else 'Alice' if score>0 else 'Bob'


print(stoneGame([1,2,3,7]))
