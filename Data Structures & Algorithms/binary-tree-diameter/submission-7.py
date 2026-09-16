# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        '''
        to get diameter we need 2 things

        1.) depth of both children for every node
        2.) calculate the addition of those for every node 

        #function 1 depth
        '''
        self.maxDiameter=0
        
        #self.length=0
        def depth(root):
            if root==None:
                return 0
            return 1+max(depth(root.left),depth(root.right))
        print(depth(root)-1)

        #.2)
        def dia(root):
            if root==None:
                return 
            self.maxDiameter=max(self.maxDiameter,depth(root.right)+depth(root.left))
            dia(root.left)
            dia(root.right)
            return
        dia(root)
        return self.maxDiameter

            

        