# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        from the description it makes me think, we need a bottom up approach because
        we need to check if every individual node is balanced, but we cant do that from above
        we can only do that once we reach the leaf nodes, then check as we go back up
        passing along the heights as we go
        '''
        self.result=True
        def dfs(root):
            if root==None:
                return 0

            left_height=0
            right_height=0

            if root.left:
                left_height= 1 + dfs(root.left)
            if root.right:
                right_height=1+ dfs(root.right)
            if abs(right_height-left_height)>1:
                print(f'found bad node @, {root.val}')
                self.result=False
            return max(right_height,left_height)
        dfs(root)
        return self.result