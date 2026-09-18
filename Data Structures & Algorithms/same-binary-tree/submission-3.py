# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.globaltrue=True
        def same(p,q):
            #base case
            #empty tree= empty tree 
            if p==None and q==None:
                return
            #tree !=empty tree

            if p and q==None or q and p==None:
                self.globaltrue=False
                return
            #or they arent equal
            if p.val!=q.val:
                self.globaltrue=False
                return
            same(p.right,q.right)
            same(p.left,q.left)
        
        same(p,q)
        return self.globaltrue