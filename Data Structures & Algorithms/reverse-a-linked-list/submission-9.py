# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #empty dummy node
        prev=None
        r=ListNode()
        r.next=head
        
        curr=head

        while curr:
           
            temp=curr.next
            
            curr.next=prev
            
            prev=curr
            print(f'prev.val: {prev.val}')
            curr=temp
            

        
        
        
        return prev

  

        