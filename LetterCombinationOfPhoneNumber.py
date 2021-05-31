'''
This Method can be done by simple recurrsion only, or it can also be done by visualizing a tree i.e dfs
method
'''

def phoneLetters(digits):
    map = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return list(map[digits[0]])

    prev = phoneLetters(digits[:-1])
    last = map[digits[-1]]

    return [s+c for s in prev for c in last]


print(phoneLetters('93'))