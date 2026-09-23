# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        dic={}
        
        index=0
        dummy=head
        while dummy:
            
            
            dic[index]=dummy
            dummy=dummy.next
            dic[index].next=None
            
            index+=1

        for x in range(index):
            print(dic[x].next)
        
        #print(dic)

        left=0
        right=index-1

        added=index-1
        while left<right or added==0:
            if added==0:
                break
            #print(f'left {left}. right {right}')
            dic[left].next=dic[right]
            added-=1
            left+=1
            if added==0:
                break
            dic[right].next=dic[left]
            added-=1
            right-=1
            if added==0:
                break

        
        return 
        