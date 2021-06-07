'''
It is also known a breadth first search
'''

def levelOrder(root):
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
        result.append(level)

    return result