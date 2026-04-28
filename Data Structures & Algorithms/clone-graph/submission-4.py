"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        the intuition behind this problem is that we want to use dfs to traverse through all of these nodes, 
        recursivley and at each point we clone the node, and we clone all of its nieghbors aswell 
        then we append those nieghbor clones to the original nodes nieghbor value passed into the dfs function
        we only want to clone nodes that arent already seen aka, nodes that arent in our
        dictionary
        '''
        clone_dictionary={}
        
        if node==None:
            return
        def dfs(node):
            
            #we want to make our base case, if our node is already cloned we just return clone and skip algorithm
            if node in clone_dictionary:
                return clone_dictionary[node]
            #if node not already clones we must clone it 
            #in the question it says deep copy, so we must create a new node with the same value
            
            clone=Node(node.val) 

            #we want to add it to the dictionary
            clone_dictionary[node]=clone

            #now we want to recursivley clone all of the nieghbors
            #lets traverse the nieghbors in our original node passed into dfs and clone its nieghbors
            for n in node.neighbors:
                #this temp will return a nieghbor clone
                temp=dfs(n)
                #we want to append this to clones nieghbors tho
                clone.neighbors.append(temp)
            return clone
        return dfs(node)