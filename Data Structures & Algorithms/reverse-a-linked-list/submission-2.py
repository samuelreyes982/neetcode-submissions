# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #create copy
        prev=None

        while head:
            #temp=head.next
            prev=ListNode(head.val,prev)
            head=head.next

        return prev
        