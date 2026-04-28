# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        '''
        we want to run dfs from the node to the point that
        we reach a leaf, at each level when we recurse we
        will simply add a 1, so we can account for each new level.
        when we reach a leaf, we will return 0

        however we have 2 branches at level, so how can we account for this
        we simply run max(left,right)
        '''

        if root == None:
            return 0
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
        