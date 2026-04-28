# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #if we havent found ancestor yet and we are at one of the vals this is the lca
        if root.val==q.val or root.val==p.val:
            return root
        #found split
        if root.val>q.val and p.val>root.val or   root.val>p.val and q.val>root.val :
            return root

        if root.val>p.val and root.val>q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        if root.val<p.val and root.val<q.val:
            return self.lowestCommonAncestor(root.right,p,q)


        