class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #we want to prevent cycles

        #lets use dfs to explore all neighbors to see if we find a cycle
        #if we find a cycle then we return false
        
        #we should build an adj list
        dic={}
        for i in range(len(edges)):
            if edges[i][0] in dic:
                dic[edges[i][0]].append(edges[i][1])
            else:
                dic[edges[i][0]]=[edges[i][1]]
            if edges[i][1] in dic:
                dic[edges[i][1]].append(edges[i][0])
            else:
                dic[edges[i][1]]=[edges[i][0]]
        print(dic)   


        seen=set()

        def dfs(root,prev):

            if root in seen:
                return False
            
            #else lets add to seen then look through its neighbors
            seen.add(root)
            if root in dic:
                for item in dic[root]:
                    if item!=prev:
                        if dfs(item,root)==False:
                            return False
                    
            #seen.remove(root)
            return
        if dfs(0,-1)==False:
            return False
        if len(seen)==n:
            return True
        else:
            return False



