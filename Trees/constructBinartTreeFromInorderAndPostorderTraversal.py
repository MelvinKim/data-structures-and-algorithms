class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def buildTree(self, preorder, inorder):
        # base case
        if not preorder or not inorder:
            return None
        
        # create a TreeNode, using preorder list first value
        root = TreeNode(val=preorder[0])
        # find position of the root node in the inorder array
        mid = inorder.index(preorder[0])
        # create the left subtree
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid])
        # create the right subtree
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root