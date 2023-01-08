class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reorderList(self, head):
        if not head:
            return head
        
        prev = None
        dummy_node = head
        tail = dummy_node
        
        # reverse the list, prev = reverse head(new head)
        while(tail):
            next_node = tail.next
            tail.next = prev
            prev = tail
            tail = next_node
            
        # build the next list
        while(tail and tail.val != prev.val):
            tail.next = prev
            tail = tail.next
            prev = prev.next
            
        return dummy_node