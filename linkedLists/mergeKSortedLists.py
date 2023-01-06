class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
class Solution(object):
    def mergeKLists(self, lists):
        if lists == None or len(lists) == 0:
            return None
        
        main_list = []
        for list in lists:
            for x in list:
                main_list.append(x)
                
        dummy_node = ListNode()
        current_node = dummy_node
        
        for x in main_list:
            new_node = ListNode(val=x)
            current_node.next = new_node
            current_node = current_node.next
        
        return dummy_node.next