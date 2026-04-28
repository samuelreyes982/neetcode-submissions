#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        '''
        we want to create a dfs that only returnsn the node if it is less then a largest node val
        in path 


        


        
        
        
        '''
       
        self.count=0       
        #recursive dsf

        if root==None:
            return 0
        def dfs(root,x):

            if root == None:
                return 0 

            maxnum=max(x,root.val)
            if root.val>=maxnum:
                maxnum=root.val
                self.count= self.count+1

            dfs(root.left,maxnum)
            dfs(root.right,maxnum)

        dfs(root,root.val)
        return self.count            
            