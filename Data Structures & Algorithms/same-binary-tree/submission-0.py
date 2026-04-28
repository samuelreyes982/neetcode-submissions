# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.bank=[]
        def dfs(root,root2):
            if root==None and root2==None:
                return True
            if root == None and root2:
                return False
            if root  and root2==None:
                return False
            if root.val != root2.val:
                return False
            left = root.left
            right= root.right

            left2 = root2.left
            right2 = root2.right

            return dfs(left,left2) and dfs(right,right2)

        return dfs(p,q)
            
            


            
