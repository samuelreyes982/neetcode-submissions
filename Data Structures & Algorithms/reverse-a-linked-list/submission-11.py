# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''

        0->none
        1->0-None


        to get to last node
        we keep going
        '''
        end=None
        while head:
            #saving the rest of the linkedlist

            nextt=head.next#next 1-2-3-None
            head.next=end# 0->None
            end=head
            head=nextt
        return end



