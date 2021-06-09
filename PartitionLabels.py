'''
In this question we use dictionary to take count of last character appeared, you'll know more by code below
'''

def partitonLabel(s):
    dic = {c:i for i,c in enumerate(s)}
    left,right=0,0
    result = []

    for i,char in enumerate(s):
        right = max(right,dic[char])

        if i == right:
            result += [right-left+1]
            left = i+1

    return result

s = "ababcbacadefegdehijhklij"
print(partitonLabel(s))