from multiprocessing import dummy


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 == None and list2 == None:
            return list1
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        
        dummy_node = ListNode()
        tail = dummy_node
        
        while(list1 and list2 ):
            if (list1.val < list2.val):
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
                
            tail = tail.next
            
        # check to ensure we have reached the end of the two lists for boths cases
        while (list1):
            tail.next = list1
            list1 = list1.next   
        while (list2):
            tail.next = list2
            list2 = list2.next
            
        return dummy_node.next