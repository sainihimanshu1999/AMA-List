'''
a binary search tree is valid when it's left child is lesser than root and right child is greater than root
'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


def bst(root):
    def dfs(node,left,right):
        if not node:
            return True
        
        if not left<node.val<right:
            return False
        
        return dfs(node.left,left,node.val) and dfs(node.right,node.val,right)

    return dfs(root,float('-inf'),float('inf'))