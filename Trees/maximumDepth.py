class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        
        leftMax = self.maxDepth(root=root.left)
        rightMax = self.maxDepth(root=root.right)
        
        return max(leftMax, rightMax) + 1

        
    