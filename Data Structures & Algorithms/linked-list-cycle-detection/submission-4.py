# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        so these are all objects, and if the object is being pointed to again
        then it has a cycle, ig we have no cycle if the tail hits null
        '''
        seen=set()

        while head:
            if head.next in seen:
                return True
            seen.add(head)
            head=head.next
        return False