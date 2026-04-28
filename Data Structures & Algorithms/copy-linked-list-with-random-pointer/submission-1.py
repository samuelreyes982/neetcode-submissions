"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic={}
        #set None to None
        dic[None]=None
        curr=head
        #saving nodes during first pass
        while curr:
            new=Node(curr.val)

            dic[curr]=new

            curr=curr.next
        # we can set out pointers on the second pass

        curr=head

        while curr:
            item=dic[curr]
            item.next=dic[curr.next]
            item.random=dic[curr.random]
            curr=curr.next
        return dic[head]


