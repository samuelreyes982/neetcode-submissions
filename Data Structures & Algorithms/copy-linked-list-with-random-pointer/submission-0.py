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
        #lets do the two pass approach with a dictionary

        #lets do our first pass
        #initialize dictionary
        #lets map None to None
        dic={None:None}

        #during the first pass we are only gonna create our copys and
        #set the key which is the original node of linkedlist to a new Node

        curr=head

        while curr:
            copy=Node(curr.val)
            dic[curr]=copy
            curr=curr.next
        #now we want to set pointers
        #essentially we are gonna link together all of our nodes
        
        #reset curr
        curr=head
        while curr:
            copy=dic[curr]
            copy.next=dic[curr.next]
            copy.random=dic[curr.random]
            curr=curr.next
        return dic[head]



