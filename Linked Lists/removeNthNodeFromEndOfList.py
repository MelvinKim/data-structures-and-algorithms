class ListNode(object):
    def __init__(self, val=0, next=None):
            self.val = val 
            self.next = next
            
            
class Solution(object):
    def removeNthNodeFromEnd(self, head, n):
        if not head:
            return head
        
        dummy_node = ListNode(0, head)
        slow = dummy_node
        fast = head
        while n > 0 and fast:
            fast = fast.next
            n -= 1
            
        while fast:
            slow = slow.next
            fast = fast.next
        
        # delete the node
        slow.next = slow.next.next
        
        return dummy_node.next