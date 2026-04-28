class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        '''
        EXAMPLE 1:
        3
        |
        |
        0-------1----4
        |
        |
        2


        EXAMPLE 2:
              -----------|
             |           |
             |           |
        0----1----2-----3
             |
             |
             4
        '''
        #i think for a tree to be valid, we dont want any
        #of our children to be connected to any of the previous
        #nodes in our tree, i mean essentially we dont want a cycle


        #we want to traverse edges and make sure that 
        

        #we just can connect to a node that is at a depth more then 1 



        #build an adjacency list
        
        #edge case where graph is empty
        if not edges:
            return True



        seen=set()
        dic={}

        for x in edges:
            
            if x[0] in dic:
                dic[x[0]].append(x[1])
                
            else:
                dic[x[0]]=[x[1]]
                
            
            if x[1] in dic:
                
                dic[x[1]].append(x[0])
            else:
                
                dic[x[1]]=[x[0]]



        print(dic)


        #we know we can return false if 
        # when traversing, we see a node weve seen before.

        def dfs(edge,prev):
           #return false if edge already in seen
            if edge in seen:
                return False


            # lets add to seen now
            seen.add(edge)
        
            #now lets traverse all our nieghbors

            for neighbor in dic[edge]:
                if neighbor !=prev:
                    if dfs(neighbor,edge)==False:
                        return False
            
            return True
        #for a graph to be a valid tree we have 2 conditions

        #1.) have no cycles

        #2.) all edges must be connected

        #we can should be able to traverse all edges from a dfs call on root
        # we must also make sure that len(seen) is equal to our number of nodfes
        # because that means we have properly traversed all nodes from our dfs call
        #print(dfs(0,-1))
        return dfs(0,-1) and len(seen)==n




        