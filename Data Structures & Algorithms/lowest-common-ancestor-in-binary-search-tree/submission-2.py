# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        to find lowst common ancestor we just need to find the split, where one is less than or one is greater then
        root

        if both are less then we need to go left
        if both are greater then we need to go right
        '''

        while root:
            if p.val<root.val and q.val<root.val:
                root=root.left
            elif p.val>root.val and q.val>root.val:
                root=root.right
            else:
                #found a split, where right and left arent both greater or less then
                return root
            