# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxdepth=0

        def dfs(root,depth):
            if root ==None:
                return
            depth=depth+1
            self.maxdepth=max(depth,self.maxdepth)

            dfs(root.left,depth)
            dfs(root.right,depth)
        dfs(root,0)

        return self.maxdepth