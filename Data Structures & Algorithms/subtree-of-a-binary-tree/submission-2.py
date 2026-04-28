# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        defininatly need the use of a helper function to check if subtree is the same tree, then we need to ask that at every
        node if not then false
        '''
        #helper
        
        
        def isSameTree(root, root2):
        #base case
            if root == None and root2 == None:
                return True
            
            if root and root2 and root.val == root2.val:
                
                return  isSameTree(root.left,root2.left) and isSameTree(root.right,root2.right)
            else:
                    return False
        
        #end helper
        
        
        if root and subRoot ==None:
            return True
        
        if root==None and subRoot:
            return False
        if isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    

    