'''
While merging two binary trees, values of overlapping nodes will be added
'''

def merge(root1,root2):
    if root1 and root2:
        root = TreeNode(root1.val+root2.val)
        root.left = merge(root1.left,root.left)
        root.right = merge(root1.right,root2.right)
        return root
    else:
        return root1 or root2