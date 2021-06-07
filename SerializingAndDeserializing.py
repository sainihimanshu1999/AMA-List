'''
In this question preorder traversal is used by serializing
'''

class Codec:

    def serialize(self,root):
        if not root:
            return 'x'
        return ','.join([str(root.val),self.serialize(root.left),self.serialize(root.right)])

    
    def deserialize(seld,data):
        self.data = data

        if self.data[0] == 'x':
            return None

        node = TreeNode(self.data[:self.data.find(',')])
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])

        return node
