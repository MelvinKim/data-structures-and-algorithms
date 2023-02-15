class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    """
    O(N) Time
    O(1) Space
    """
    def hasCycleOptimal(self, head):
        if not head:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False 
    """
    O(N) Time
    O(N) Space
    
    - we add the nodes itself to the hashmap, not the node's value --> since we could a multiple nodes with same value
    - but different next pointers
    - you can't use node's val as key, since the value is an integer
    """   
    def hasCycleUsingHashmap(self, head):
        if not head:
            return False
        
        map = {}
        while head:
            if head in map:
                return True
            
            map[head] = 1
            head = head.next
            
        return False

        