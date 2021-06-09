'''
We have two way of doing this question, one is through simple dictionary which will give O(nlogn) time complexity 
and other one is by using heaps, it will give us O(nlogK) time complexity
'''

#basic dictionary

def topK(words,k):
    dic = {}
    for word in words:
        dic[word] = dic.get(word,0)+1

    res = sorted(dic, key=lambda word:(-dic[word],word))
    return res[:k]


#using heaps

from collections import Counter
from heapq import nsmallest
import heapq


def topK2(words,k):
    freq = Counter(words)
    return heapq.nsmallest(k,freq,key=lambda word:(-freq[word],word))

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3
print(topK2(words,k))