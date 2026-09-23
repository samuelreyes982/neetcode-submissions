# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        we are gonna go from left to right, and since this is a level order teraversalm we are gonna 
        use bfs, which is a level at a time instead of dfs which is reaching the deepest node before exploring other        nodes.
        '''
        q=collections.deque()

        result_list=[]


        q.append(root)

        while q:
            q_len=len(q)
            level=[]
            for i in range(q_len):
                item=q.popleft()
                if item:
                    
                    level.append(item.val)
                    if item.left:
                        q.append(item.left)
                    if item.right:
                        q.append(item.right)
            if len(level)>=1:
                result_list.append(level)
        return result_list