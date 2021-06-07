'''
Basic recursion, using dictionary to store the elements
'''

def frequent(root):
    if not root:
        return []


    def dfs(node):
        if not node:
            return 0

        sumi = node.val + dfs(node.left) + dfs(node.right)

        dic[sumi] = dic.get(sumi,0)+1
        return sumi


    dic ={}
    dfs(root)
    maxval = max(dic.values())
    return [s for s in dic if dic[s] == maxval]