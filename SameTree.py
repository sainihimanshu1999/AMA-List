'''
To check wheter the tree is same or not, we have to equate values at every level
'''

def sameTree(p,q):
    if p and q:
        return p.val == q.val and sameTree(p.left,q.left) and sameTree(p.right,q.right)

    else: 
        return p == q