# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        '''
        this one seems a little tricky. i think our strategy 
        will be find the naive solution first and optimize after 

        1.) our step should be recurse on every node of root

        2.) check on that node if it is equal to subroot
        '''

        #first lets make function to check if same

        def same(p,q):
            #base cases
            if p==None and q==None:
                return True

            if (p and not q) or (q and not p):
                return False
            if p.val !=q.val:
                return False
            #test
            return all([same(p.right,q.right),same(p.left,q.left)]) 



        def search(root):
            if root==None:
                return False
            if same(root,subRoot):
                return True
            return any([search(root.left),search(root.right)])
        
        return search(root)
        