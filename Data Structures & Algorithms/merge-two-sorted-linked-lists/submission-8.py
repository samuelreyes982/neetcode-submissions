# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:



        #base case
        '''
        l1: None l2: None

        return None


        l1: 1 l2: 2
        '''
        l1=list1
        l2=list2
        
        result = ListNode()
        pointer=result
        while l1 and l2:
            print(f'l1.val: {l1.val}.   l2.val: {l2.val}')
            if l1.val <= l2.val:
                temp=l1.next
                l1.next=None
                result.next=l1
                result=result.next
                l1=temp
                #continue
            elif l1.val > l2.val:
                
                temp=l2.next
                l2.next=None
                result.next=l2
                result=result.next
                l2=temp
                #continue
        #print(l1)
        #print(l2)  
        # add remaining list if applicable
        #result=result.next
        print(result.val)
        
        if l1 and not l2:
            result.next=l1 
            #result=result.next 
        if l2 and not l1:
            result.next=l2 
            #result=result.next
           
        return pointer.next