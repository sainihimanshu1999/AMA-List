'''
In this question we are making two functions, first one to traverse the both the trees to find the initial subtree.
Other one is to check the subtree found is equal to the subtree we are given
'''

def subTree(root,subRoot):
    if not subRoot: return True

    def dfs(node1,node2):
        if not node1:
            return False

        if node1.val == node2.val and check(node1,node2):
            return True

        return dfs(node1.left,node2) or dfs(node1.right,node2)

    
    def check(node1,node2):
        if not node1 and not node2:
            return True

        elif node1 and not node2 or node2 and not node1:
            return False

        if node1.val != node2.val:
            return False

        return check(node1.left,node2.left) and check(node1.right,node2.right)

    return dfs(root,subRoot)