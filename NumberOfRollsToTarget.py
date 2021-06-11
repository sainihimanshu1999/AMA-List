'''
We use dynamic programming approach in this question (by really just dividing problem in the smaller sub problem)
'''

def rolls(dice,faces,target):
    memo = {}

    def dp(d,target):
        if d == 0:
            return 0 if target>0 else 1
        if (d,target) in memo:
            return memo[(d,target)]

        result = 0
        for k in range(max(0,target-faces),target):
            result += dp(d-1,k)

        memo[(d,target)] = result
        return result
    
    return dp(dice,target)%(10**9+7)


print(rolls(2,5,10))