class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseListBruteForce(self, head): # counter-check this --> not very sure
        if head == None:
            return head
        
        stack = []
        while(head != None):
            stack.append(head)
            head = head.next
          
        current_head = None  
        temp_head = current_head
        while(stack):
            # pop from the end
            for i in range(len(stack)-1, 0, -1):
                current_head = stack[i]
                current_head = current_head.next
                
        return temp_head
                
    """
    O(N) Time complexity
    O(1) Space complexity
    """
    def reverseListIterativeOptimal(self, head):
        if head == None:
            return head
        
        prev = None
        current = head
        
        while current:
            next = current.next # to enable us keep track of the next node, since we are breaking that link
            current.next = prev
            prev = current
            current = next
               
        return prev
    
    """
    0(N) Time complexity
    O(N) Space complexity
    - TODO:  go through this again :)
    """
    def reverseListRecursiveOptimal(self, head):
        # base case --> if head == null (None)
        if not head:
            return None
            
        newHead = head
        if head.next:
            newHead = self.reverseListRecursiveOptimal(head.next)
            head.next.next = head
            
        head.next = None
        return newHead        
        
    
# my initial working
# def reverseListBruteForce(self, head):
#         if head == None:
#             return head
        
#         stack = []
#         while(head != None):
#             stack.append(head)
#             head = head.next
          
#         current_head = None  
#         temp_head = current_head
#         while(stack):
#             # pop from the end
#             for i in range(len(stack)-1, 0, -1):
#                 current_head = stack[i]
#                 current_head = current_head.next
                
#         return temp_head
                
    
#     # optimal
#     def reverseListOptimal(self, head):
#         if head == None:
#             return head
        
#         prev = None
#         current = head
#         next = head.next
        
#         while(current != None or current.next != None):
#             current.next = prev
#             prev = current
#             current = next
#             next = current.next
            
#         return current