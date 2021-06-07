
'''
In this question we are using variable sliding window (sliding window is applied using two pointers)
'''
import collections

def minWinSub(s,target):
    target_counter = collections.Counter(target)
    target_length = len(target)
    start,end =0,0
    minWindow = ''

    for end in range(len(s)):
        if target_counter[s[end]]>0:
            target_length -=1
        
        target_counter[s[end]] -=1

        while (target_length==0):
            window_len = end-start+1
            if not minWindow or window_len<len(minWindow):
                minWindow = s[start:end+1]

            target_counter[s[start]] +=1

            if target_counter[s[start]]>0:
                target_length +=1

            start +=1
    return minWindow


s,t = "ADOBECODEBANC", "ABC"
print(minWinSub(s,t))
             