# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root==None:
            return
    
            
        
        
        
        #only saving values if we have a right and a left
        
        
        
        
        temp=root.right
    
        root.right=root.left
        root.left=temp


        self.invertTree(root.left)
        self.invertTree(root.right)
        return root



'''
                    3
                |       |
            null        1
                     |      |   
                    2       null









'''

