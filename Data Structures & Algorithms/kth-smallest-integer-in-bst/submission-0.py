# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        naive approach is to just visit each node, add the values to a list, then sort list and return the index

        '''
        self.globalist=[]
        def dfs(root):
        
            if root==None:
               return 
            self.globalist.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        self.globalist.sort()
        print(f'list {self.globalist}')
        return self.globalist[k-1]             

        