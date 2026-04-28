# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        '''
        1.) make some kind of list that will hold the results of level nodes

        2.) use bsf, aka use a queueing algo in order to get this achieved result

        3.) make sure to queue the child nodes of node when popping from queue

        
        '''
        
        
        # we will be returning this list as it holds with nested lists
        return_list=[]



        #edge case
        if root==None:
            return return_list

        #now create queue, in python we can use deque which is a double ended queue

        q=collections.deque()

        #initialize q with root of binary tree

        q.append(root)

        #start algorithm so that we can traverse all nodes

        while q:

            #for every level
            level=[]
            for _ in range(len(q)):
                
                item=q.popleft()
                #append to level
                if item:
                    level.append(item.val)
                

                #check if children, add them to queue
                if item.left:
                    q.append(item.left)

                if item.right:
                    q.append(item.right)
                
                #add level to return list

            return_list.append(level)
        return return_list





        

        