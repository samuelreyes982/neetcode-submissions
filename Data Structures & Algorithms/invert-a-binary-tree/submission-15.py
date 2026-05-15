# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #base case where if we had a single leaf, there would be no need
        #switch leafs that dont exist, thus we should return
        if root==None:
            return root
        
        #else, lets switch our leaf nodes
        temp=root.left
        root.left=root.right
        root.right=temp


        #now we need to keep going, down our tree
        #recursive call function on our children

        self.invertTree(root.left)  
        self.invertTree(root.right)

        return root

