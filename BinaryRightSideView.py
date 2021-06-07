'''
This question can be done by two ways, one by dfs and bfs
'''

#dfs way

def rightside(root):
    if not root: return []
    def dfs(node,depth):
        if depth == len(result):
            result.append(node.val)
        
        dfs(node.right,depth+1)
        dfs(node.left,depth+1)

    result = []
    dfs(root,0)
    return result


#bfs way

def rightSide(root):
    if not root:
        return []

    q = [root]
    result = []
    while q:
        level = []
        for i in range(len(q)):
            node = q.pop(0)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level.append(node.val)
        result.append(level[-1])
    return result