# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:
            return None
        
        list_size = 0
        dummy = head
        
        while dummy:
            list_size += 1
            dummy = dummy.next
            
        k = k % list_size
        
        for _ in range(k):
            dummy = head
            while dummy and dummy.next:
                if dummy.next.next == None:
                    last_element = ListNode(dummy.next.val)
                    dummy.next = None
                    last_element.next = head
                    head = last_element

                dummy = dummy.next
                
        return head
