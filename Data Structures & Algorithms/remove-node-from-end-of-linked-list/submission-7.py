# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dic={}

        curr=head
        i=1
        #stored our values
        while curr:
            dic[i]=curr
            curr=curr.next
            i+=1
        
        #init before and after
        dic[0]=ListNode('inf')
        dic[0].next=dic[1]
        
        dic[i]=None
        
        print(f'dictionary {dic}')
        print(f'i : {i}')
        #swap aka replace
        replace=i-n
        before_last=dic[replace-1]
        before_last.next=dic[replace+1]

        return dic[0].next
        
            
        