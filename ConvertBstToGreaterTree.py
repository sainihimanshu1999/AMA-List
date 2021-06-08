'''
Greater tree means coverting every node value to the sum of all the greater values(greater than the current node) present
in the tree
'''

def greaterTree(root):
    self.sumi = 0
    def dfs(node):
        if not node: return None

        dfs(node.right)
        self.sumi += node.val
        node.val = self.sumi
        dfs(node.left)
        return node

    return dfs(root)