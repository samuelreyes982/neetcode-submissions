# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        '''
        0->1->2->3

        3->2->1->0



        0->None
        
        '''
        
        
        
        new=None
        

        while head!=None:
            temp=head.next #temp = 1->2->3
            head.next=new # 0->None
            new=head# new= 0->None
            head=temp# head= 1->2->3
        return new    
            