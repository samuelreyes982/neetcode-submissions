# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxx=0

        def dfs(root):
            if root==None:
                return 0
            left=0
            right=0
            if root.left:
                left= 1+dfs(root.left)
            if root.right:
                right=1+dfs(root.right)
            self.maxx=max(left+right,self.maxx)
            return max(left,right)
        dfs(root)
        return self.maxx  


        