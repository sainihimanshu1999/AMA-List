'''
Just constructing a string from binary
'''


def treetostring(root):
    if not root: return ''
    result = ''

    left = treetostring(root.left)
    right = treetostring(root.right)

    if left or right:
        result += '(%s)'%left
    if right:
        result += '(%s)'%right

    return str(node.val)+result