'''
In this question we have to find all the anagrams in my string. We use counters or dict to have count of all the letters 
present, if the count of letter is equal then it's the anagram
'''
from collections import Counter

def anagram(s,p):

    Pcount = Counter(p)
    Scount = Counter(s[:len(p)])

    result = []
    i=0
    j=len(p)

    while j<=len(s):

        if Pcount == Scount:
            result.append(i)

        Scount[s[i]] -= 1

        if Scount[s[i]] <=0:
            Scount.pop(s[i])

        if j<len(s):
            Scount[s[j]] +=1
        
        i+=1
        j+=1
    return result

s = "cbaebabacd"
p = "abc"

print(anagram(s,p))