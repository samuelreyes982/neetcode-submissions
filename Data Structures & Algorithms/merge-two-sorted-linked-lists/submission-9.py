# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        plan so we are gonna have a pointer to each head, compare them, and then we are
        gonna keep setting the the 

        1->none


        l1: 2-4
        l2: 1-3-5


        1->1

        '''
        l1=list1
        l2=list2
        pointer=ListNode()
        pointer2=pointer
        while l1 and l2:
            print(f'l1 val {l1.val}')
            print(f'l2 val {l2.val}')
            next1=l1.next
            next2=l2.next
            if l1.val<=l2.val:
                pointer.next=l1
                l1=next1
                
            elif l2.val<l1.val:
                pointer.next=l2
                l2=next2
                
            
            pointer=pointer.next
        
        #print(l1)
        #print(l2)
        if l1 and not l2:
            pointer.next=l1
        if not l1 and l2:
            pointer.next=l2

        return pointer2.next

        