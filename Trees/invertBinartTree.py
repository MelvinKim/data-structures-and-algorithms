from logging import root


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def invertTree(self, root):
        if not root:
            return root
        
        # swapping
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root=root.left)
        self.invertTree(root=root.right)
        
        return root
       
    
"""
flipping / swapping the nodes at each layer

# one way
def invertTree(self, root):
        if not root:
            return root
        
        left = self.invertTree(root=root.left)
        right = self.invertTree(root=root.right)
        
        # swap
        root.left = right
        root.right = left
        
        return root
        
"""