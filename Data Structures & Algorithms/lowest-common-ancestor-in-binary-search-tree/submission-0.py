# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
        '''
        we want to start with base case, which is a node can be the descendent of itself
        i guess the intutition is that keep searching down the tree only if both nodes 
        are on one side, aka if both smaller nodes are greater or less then 
        the current node, else there is a split and if there is a split we should
        return that node

        '''
        curr= root

        #iterate so that we can keep searching
        while curr:

            #identifying split
            if p.val >= curr.val and curr.val>= q.val:
                return curr
            #identifying split part 2
            if p.val <= curr.val and curr.val<= q.val:
                return curr
            
            if curr.val>p.val and curr.val>q.val:
                curr=curr.left
            if curr.val <p.val and curr.val <q.val:
                curr=curr.right

