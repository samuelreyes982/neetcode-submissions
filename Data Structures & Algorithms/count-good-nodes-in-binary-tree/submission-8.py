# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        self.count=0

        def dfs(root,running_max):


            if root==None:
                return

            running_max=max(root.val,running_max)

            if root.val>=running_max:
                self.count+=1

            dfs(root.right,running_max)
            dfs(root.left,running_max)
            return
        dfs(root,root.val)
        return self.count