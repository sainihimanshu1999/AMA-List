

def evengrandparent(root):
    self.sumi = 0
    def dfs(node,parent,grandparent):
        if not node: return 0

        if parent and grandparent and grandparent.val%2==0:
            self.sumi += node
        dfs(node.left,node,parent)
        dfs(node.righ,node,parent)

    dfs(root,None,None)
    return self.sumi
    