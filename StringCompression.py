'''
In this question we have to compress a string and wrtie it's frequency number in front of it and then return the length
of the array
'''

def compress(s):
    slow,fast =0,0
    n = len(s)

    while fast<n:
        s[slow] = s[fast]
        count = 1

        while fast+1<n and s[fast]==s[fast+1]:
            fast +=1
            count +=1

        if count>1:
            for c in str(count):
                s[slow+1] = c
                slow+=1

        slow+=1
        fast+=1
    return slow


chars = ["a","a","b","b","c","c","c"]
print(compress(chars))