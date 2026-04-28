# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        
        
        list=[]
        
        #empty root edge case
        if root == None:
            return list

        q=collections.deque()
        q.append(root)
        
        while q:
            level=[]
            qlen=len(q)

            print(f'qlen: {qlen}')

            for _ in range(qlen):
                item=q.popleft()
                
                
                if item:
                    level.append(item.val)
                    print(f'level appended : {item.val}')
                    if item.left:
                        q.append(item.left)
                        print(f'q appended : {item.left.val}')
                    if item.right:
                       q.append(item.right)
                       print(f'q appended : {item.right.val}')

            list.append(level)
        
        
        
        
        return list
            

        