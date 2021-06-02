'''
used basic memoization
'''

def wordBreak(s,wordDict):
    def func(s,wordDict,memo):
        if s in memo:
            return memo[s]

        for word in wordDict:
            if s[:len(word)] == word:
                if len(s) == len(word):
                    memo[s] = True
                    return True

                else:
                    suffix = s[len(word):]
                    if func(suffix,wordDict,memo):
                        memo[s] =True
                        return True
        memo[s] = False
        return memo[s]

    return func(s,wordDict,{})
    

s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

print(wordBreak(s,wordDict))