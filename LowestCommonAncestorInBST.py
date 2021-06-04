'''
In BST we take in account that left subtree is smaller than right one
'''

def LCA(root,p,q):
    if not root or not p or not q:
        return None

    if max(p.val,q.val)<root.val:
        return LCA(root.left,p,q)
    elif min(p.val,q.val)>root.val:
        return LCA(root.right,p,q)
    else:
        return root