# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dictionary={}
        i=1
        pointer=head
        while pointer:
            
            dictionary[i]= pointer
            pointer=pointer.next
            i+=1
        #print(dictionary)
        index=len(dictionary)-n+1
        #print(index)

        
        #add buffer
        dictionary[0]=ListNode('',dictionary[1])
       
        dictionary[len(dictionary)]=None
        #dictionary[len(dictionary)-1].next=dictionary[len(dictionary)]
        dummy=dictionary[0]
        print(dummy.next.val)
         
        dictionary[index-1].next=dictionary[index+1]
        
        return dummy.next
