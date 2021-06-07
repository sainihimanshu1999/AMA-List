'''
This question can be done by two methods, one is by enumerate and other is just by using while loop
'''

#enumerate

def lgsub(s):
    seen = {}
    start = 0
    max_len = 0
    for i,v in enumerate(s):
        if v in seen and start<=seen[v]:
            start += seen[v] +1

        else: 
            max_len = max(max_len,i-start+1)
        seen[v] = i

    return max_len


#while loop

def longSub(s):
    seen = {}
    start = 0
    max_len = 0
    i = 0 
    while i<len(s):
        if s[i] in seen and start <= seen[s[i]]:
            start = seen[s[i]]+1
        else:
            max_len = max(max_len,i-start+1)

        seen[s[i]] = i
        i+=1
    return max_len
        