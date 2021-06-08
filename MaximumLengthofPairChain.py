'''
Pair length 
'''

def pairChain(pairs):
    curr,result = float('-inf'),0
    pairs = sorted(pairs, key=lambda x:x[0])

    for p in pairs:
        if curr<p[0]:
            curr,result = p[1],result+1

    return result


pairs = [[1,2],[2,3],[3,4]]
print(pairChain(pairs))
