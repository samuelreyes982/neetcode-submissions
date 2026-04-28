class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if n==1:
            return 1
        dic={}
        seen=set()
        self.cc=0
        for j in range(n):
            dic[j]=[]
        for i in range(len(edges)):
            if edges[i][0] in dic:
                dic[edges[i][0]].append(edges[i][1])
            

            if edges[i][1] in dic:
                dic[edges[i][1]].append(edges[i][0])
           
        print(dic)



        def dfs(root):

            #cycle detection
            if root in seen:
                return 
            #else we add to seen and explore neighbors


            seen.add(root)


            if root in dic:
                for item in dic[root]:
                    dfs(item)

            
            return
        for item in dic :
            if item not in seen:
                dfs(item)
                self.cc+=1
        print(self.cc)        
        return self.cc 



