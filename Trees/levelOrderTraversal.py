import collections
from unittest import result


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def levelOrder(self, root):
       res = []
       
       queue = collections.deque()
       queue.append(root)
       
       while queue:
           queueLen = len(queue)
           level = []
           for i in range(queueLen):
               node = queue.popleft()
               if node:
                   level.append(node.val)
                   # add the children
                   if node.left:
                        queue.append(node.left)
                   if node.right:
                        queue.append(node.right)
           if level:
                res.append(level)
                        
                        
       return res
           
           
       
        
"""
Breadth First Search can be implemented using a Queue
BFS == level order traversal
"""