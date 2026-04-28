# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result=[]

        q=collections.deque()
        #add root node always to the queue
        q.append(root)
        # now we are going to do a bfs 
        while q:
            level=[]
            for i in range(len(q)):
                #print(q.popleft())
                node=q.popleft()
                if node:
                    right=node.right
                    left=node.left
                    q.append(left)
                    q.append(right)
                    level.append(node.val)
            if level!=[]:
                result.append(level)
        return result

        