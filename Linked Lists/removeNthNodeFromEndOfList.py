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
    
    def removeNthNodeFromEndBruteForce(self, head, n):
        if not head:
            return head
        
        dummy_node = ListNode(val=0)
        dummy_node.next = head
        current_node = dummy_node
        
        # find the number of nodes
        count_head = head 
        count = 0
        while count_head:
            count += 1
            count_head = count_head.next
            
        val = count - n 
        while val > 0:
            current_node = current_node.next
            val -= 1
        
        temp_node = current_node.next.next
        current_node.next = temp_node
        return dummy_node.next