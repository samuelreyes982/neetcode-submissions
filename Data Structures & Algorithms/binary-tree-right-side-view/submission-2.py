# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        looks like we are trying to find the right most node at each level.
        this means we need to use bsf. then pop to the right. and then disgard the left of the queue
        '''

        return_list = []


        if root==None:
            return return_list

        q=collections.deque()

        #initialize queue
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                item=q.popleft()

                if item:
                    level.append(item.val)
                
                if item.left:
                    q.append(item.left)
                
                if item.right:
                    q.append(item.right)
            return_list.append(level)
        
        #looks like we created a normal level order, now to get right side view, we can simply
        #take the right most element at each level

        rightlist=[x[-1] for x in return_list]

        return rightlist
                
            
                





