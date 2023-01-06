class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def lowestCommonAncestorIterative(self, root, p, q):
        cur = root 
        while cur:
            # p and q values are greater than the root check the right side of the tree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
            
    def lowestCommonAncestorRecursive(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            self.lowestCommonAncestorRecursive(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            self.lowestCommonAncestorRecursive(root.right, p, q)
        else:
            return root
    
    
    
    

"""
watch Tushar video explanation: https://www.youtube.com/watch?v=TIoCCStdiFo
"""