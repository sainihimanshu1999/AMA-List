'''
Basic dfs
'''

def bstToGst(root):
    sumi = 0

    def dfs(node):
        if not node: return 0

        dfs(node.right)
        sumi += node.val
        node.val = sumi
        dfs(node.left)

    dfs(root)
    return root

        