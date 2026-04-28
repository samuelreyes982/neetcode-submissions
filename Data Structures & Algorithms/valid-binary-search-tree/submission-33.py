# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        '''
        valid binary search tree

        2. (-inf<2<inf)
        | |
        1 3
        (-inf<1<2). (2<3<inf)  
        '''

        def dfs(left_bound,root,right_bound):

            if root==None:
                return True
            if root.val<=left_bound or root.val>=right_bound:
                return False
            return dfs(left_bound,root.left,root.val) and dfs(root.val,root.right,right_bound)

        return dfs(float('-inf'),root,float('inf'))