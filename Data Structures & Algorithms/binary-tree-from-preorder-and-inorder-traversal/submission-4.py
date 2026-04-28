# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder==[] or inorder==[]:
            return None
        print(f'preorder {preorder}')
        new=TreeNode(preorder[0])
        rooti= inorder.index(preorder[0])
        new.left=(self.buildTree(preorder[1:1+rooti], inorder[:rooti]))
        new.right=(self.buildTree(preorder[rooti+1:], inorder[rooti+1:]))
        return new

        