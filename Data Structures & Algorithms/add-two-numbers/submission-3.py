# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy


        carry=0

        while l1 or l2 or carry:
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0

            #make sure to get carry 
            new=v1+v2+carry
            carry=new//10
            new=new%10
            
            new_node=ListNode(new)

            # update pointers
            if l1:
                l1=l1.next
            
            if l2:
                l2=l2.next

            curr.next=new_node
            curr=curr.next
        return dummy.next
        