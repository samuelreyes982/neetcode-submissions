"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        dic={}
        def dfs(curr_node):
            #prevents recursive calls
            
            if curr_node==None:
                return None
            
            
            if curr_node in dic:
                return dic[curr_node]
            
            #else lets create our new unseen node'

            new_node=Node()
            new_node.val=curr_node.val

            #lets add it to our dictionary now that weve created it

            dic[curr_node]=new_node


            #now we need to deal with our nieghbors in that adj list

            #we can recursivley call dfs on each one

            for n in curr_node.neighbors:
                new_node.neighbors.append(dfs(n))

            #we want to return our clone
            return new_node
        return dfs(node)

        