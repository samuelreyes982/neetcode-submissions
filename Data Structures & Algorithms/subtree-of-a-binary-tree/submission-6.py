# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root and not subRoot:
            return True
        if subRoot and not root:
            return False
        if Solution.is_sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def is_sameTree(p,q):
        if p==None and q==None:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
        if p.val!=q.val:
            return False
        return Solution.is_sameTree(p.left,q.left) and Solution.is_sameTree(p.right,q.right)
        