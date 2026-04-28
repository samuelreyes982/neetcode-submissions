class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #first we need to create an adjacency list
        
        dic={}
        seen=set()
        self.num_components=0
        for i in range(n):
            dic[i]=[]

        for item in edges:
            dic[item[0]].append(item[1])
            dic[item[1]].append(item[0])
        #print(dic)

        def dfs(node,prev):
            if node in seen:
                return
            seen.add(node)

            print(node)
            #print(dic[node])
            for neighbor in dic[node]:
                
                if neighbor!=prev:
                    dfs(neighbor,node)
            
            return True
        

        for i in range(n):
            if dfs(i,-1):
                self.num_components+=1



        return self.num_components
        