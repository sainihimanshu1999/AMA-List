'''
This question is sort of opposite of wordBreak 1, we use memoization technique in this too
'''

def concat(words):
    words = set(words)
    memo = {}

    def dfs(word):
        if word in memo:
            return memo[word]
        
        for index in range(1,len(word)):
            prefix,suffix = word[:index],word[index:]
            if prefix in words and suffix in words or prefix in words and dfs(suffix):
                memo[word] =True
                return True
        memo[word] = False
        return False

    return [word for word in words if dfs(word)]


words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(concat(words))