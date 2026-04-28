# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        basically it is find max depth with a twist
        where you need a nested function
        '''

        #track max diameter
        #declare class var so it is global
        self.globalvar=0

        #find max depth for each subtree
        def dfs(tree):
            if tree==None:
                return 0
            
            left=dfs(tree.left)
            right=dfs(tree.right)
            #diameter is the hieght of left + right
            #comparing old max and potential new max
            self.globalvar=max(self.globalvar, right+left)

            return 1 + max( left , right)
        dfs(root)
        return self.globalvar




        