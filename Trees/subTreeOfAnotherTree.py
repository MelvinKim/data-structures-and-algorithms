class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root == subRoot:
            return True
        if ((not root and subRoot) or (root and not subRoot) or (root.val != subRoot.val)):
            return False
        
        return self.isSubtree(root.left, subRoot.left) and self.isSubtree(root.right, subRoot.right)