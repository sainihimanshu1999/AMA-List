'''
Intution: if root == q or root == p return the root, if not, recurr in left nad right subtree, if your
find both then also return root but if your find only one return the found one, as we don't need to waste
computation we beacuse we know the next will be somewhere below it
'''

def LCA(root,p,q):
    if root == p or root == q:
        return root

    left=right=None

    if root.left:
        left = LCA(root.left,p,q)
    
    if root.right:
        right = LCA(root.right,p,q)

    if left and right:
        return root
    
    if left or right:
        return left or right