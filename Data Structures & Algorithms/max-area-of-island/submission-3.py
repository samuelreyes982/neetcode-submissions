class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        '''
        this is the same as the normal number of islands question, however maybe
        instead of returning the number of islands, we have a recurive call and then add all of those, when dealing
        with a specific island discovery, using that calculation we then compare it to the current max
        and update it if bigger
        '''
        

        #define boundaries create seen set
        seen=set()
        rows=len(grid)
        cols=len(grid[0])
        self.max_area=0
        num_islands=0

        self.temp_area=0
        #traverse every node in our graph

        #creating our dfs that finds all adjacent nodes in our island recursivley until it hits boundaries
        #then it returns the number of adjacent nodes-aka area
        def dfs(row,col):
            #we want to check boundaries of our recursive calls
            #negating all bad out of bounds calls to dfs
            if row>rows-1 or row<0 or col>cols-1 or col<0:
                return 
            # we dont want to infinitly check our nieghbors so we check if they are in seen
            key=tuple([row,col])

            if key in seen or grid[row][col]==0:
                return 
            #mark as seen
            seen.add(key)    
            print(f'seen added the node row: {row} col:{col}')
            #if it is a 1 node, we want to add 1 plus all potential nieghbors
            self.temp_area+=1

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)

             


        for row in range(rows):
            for col in range(cols):
                key=tuple([row,col])
                print(f'looping at : {row} col:{col}  key not in seen = {key not in seen}')
                if grid[row][col]==1 and key not in seen:
                    print(f'checking if island the node row: {row} col:{col}')
                    #we want our dfs to return the area of our island
                    dfs(row,col)
                    self.max_area=max(self.temp_area,self.max_area)
                    num_islands+=1
                    self.temp_area=0
        print(num_islands)
        return self.max_area    





