# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        initial intuition is to compute hieght of left and right on the 
        original root, then if the hieghts of left and right differ by
        more then one then return false, if not then return true

        '''
        self.maxdiff=0

        def dfs(root):
            if root==None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            diff=abs(left-right)
            self.maxdiff= max(self.maxdiff,diff)

            return 1+max(left,right)

        #we must update the difference in subtree for every root 
        # we can store the max as the global counter
        

        dfs(root)
        print(f'max diff {self.maxdiff}')
        return self.maxdiff <= 1



        