# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        '''

        i think we can use a data structure like a set to just store values and 
        if we see a listnode weve already seen before in set we return True
        '''
        seen=set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head=head.next
        return False

        