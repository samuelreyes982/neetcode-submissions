# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        '''
        for each node we need to 
        1.) find max depth of left and right trees
        2.) find out if they differ by more then 1
        '''
        self.bal=True

        #1.) find max depth of a subtree

        def maxDepth(root):
            if root==None:
                return 0
            
            
            
            return 1+max(maxDepth(root.left),maxDepth(root.right))

        print(maxDepth(root)-1)



        def differ(root):
            if root==None:
                return 
            #print(f'right {maxDepth(root.right)}  left {maxDepth(root.left)}')
            if abs(maxDepth(root.right)-maxDepth(root.left))>1:
                self.bal=False
            differ(root.left)
            differ(root.right)
            return
        differ(root)
        return self.bal