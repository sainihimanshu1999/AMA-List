'''
We question of paths in given, give extra care to, if it's root leaf included or not
'''

def pathSum(root,targetSum):
    result = []
    dfs(root,targetSum,[],result)
    return result

def dfs(node,target,path,result):
    if not node:
        return 0
    if not node.left and not node.right and node.val == target:
        path.append(node.val)
        result.append(path)
        return result

    dfs(node.left,target-node.val,path+[node.val],result)
    dfs(node.right,target-node.val,path+[node.val],result)
