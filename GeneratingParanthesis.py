'''
Visualize this question like a tree and then apply dfs, dfs searches for each and every path.
'''

def paran(n):
    if not n: 
        return []

    left,right = n,n
    result = []
    dfs(left,right,result,'')
    return result

def dfs(left,right,result,path):
    if right<left: 
        return
    
    if not left and not right:
        result.append(path)

    if left:
        dfs(left-1,right,result,path+'(' )
    if right:
        dfs(left,right-1,result,path+')')

print(paran(9))

    