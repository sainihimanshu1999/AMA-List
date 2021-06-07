'''
we have to convert root to leaf path in number and them  give the sum of all paths
'''

def sumNumbers(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return root.val

    if root.left:
        root.left.val = root.val*10+root.left.val

    if root.right:
        root.right.val = root.val*10+root.right.val

    return sumNumbers(root.left)+sumNumbers(root.right)