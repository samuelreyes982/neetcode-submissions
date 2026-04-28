class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        #first lets create an adjacency list

        adj={}

        seen=set()
        self.res=[]
        for i in range(1,len(edges)+1):
            adj[i]=[]
        print(adj)
        for item in edges:
            adj[item[0]].append(item[1])
            adj[item[1]].append(item[0])

        print(adj) 


        #we can run dfs, and go through all adj edges, and if we 
        #find somthing we have seen before, we return that node
        #we probabably need a prev value too

        def dfs(node,prev):
            print(f'node: {node}.   prev: {prev}')
            if node in seen:
                print(f'seen this {node}')
                self.res.append(sorted([node,prev]))
                return False
                
            if len(seen) >= len(edges):
                print('len seen {len(seen)}')
                return False
            
            seen.add(node)
            
            for neighbor in adj[node]:
                if neighbor!=prev:
                    if dfs(neighbor,node)==False:
                        return
                        
            return
        
        dfs(len(edges),-1)
        # iterate backwords
        print(f'self.res: {self.res}')

        for i in range(1,len(edges)):
            seen=set()
            dfs(i,-1)

        for i in range(len(edges)-1,-1,-1):
            if edges[i] in self.res:
                return edges[i]
