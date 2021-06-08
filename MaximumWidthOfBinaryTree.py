'''
Maximum width of binary tree is counted by R-L+1, we right is 2*(level+1) and left is 2*(level)
'''

def width(root):
    if not root: return 0
    queue = [(root,0)]
    result = 0

    while queue:
        result = max(result,queue[-1][1]-queue[0][1]+1)
        temp = []

        for node,i in queue:
            if node.left:
                temp.append((node.left,2*i))
            if node.right:
                temp.append((node.right,2*i+1))

        queue = temp

    return result