class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        
        Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.
        
        A valid binary search tree satisfies the following constraints:
        The left subtree of every node contains only nodes with keys less than the node's key.
        The right subtree of every node contains only nodes with keys greater than the node's key.
        Both the left and right subtrees are also binary search trees.
        
        
        
        
        '''



        def dfs(root,left_bound,right_bound):
            
            
            if root==None:
                return True
            #check if val is within boundaries
            print(f'node : {root.val}')
            if root.val <= left_bound or root.val >= right_bound:
                return False
            return dfs(root.left,left_bound,root.val) and dfs(root.right,root.val,right_bound)



            
        return dfs(root,float('-inf'),float('inf'))     