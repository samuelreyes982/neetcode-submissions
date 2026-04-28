# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            '''
            example time:

            [2]->[4]->[6]->[8]->[None]

            iterate through the list, 
            record all values and length
            store in an array, then from the backwards
            build a new linked list

            '''
            node_pointers=[]

            curr=head
            #print("here")
            while curr:
                node_pointers.append(curr)
                curr=curr.next

            left=0
            right=len(node_pointers)-1
            while left<right:
                node_pointers[left].next=node_pointers[right]
                left+=1

                if left>=right:
                    break
                node_pointers[right].next=node_pointers[left]
                right-=1
            node_pointers[left].next=None
            
            