class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #first lets define bounds

        len_row= len(grid)

        len_col=len(grid[0])
        
        seen=set()
        
        #counter
        self.number_of_islands=0

        def dfs(row,col):
            #base case/ create bounds
            if row>len_row-1 or row<0 or col>len_col-1 or col<0:
                return
            #we want to make sure the value at location is actually 1
            if grid[row][col]=='0':
                return
            #we want to make sure we mark this as visited, so we know its part of the island
            #we currently are checking and also to not keep recursing over this point
            key=tuple([row,col])
            if key in seen:
                return
            seen.add(key)

            

            #if it is a valid location, we want to check all the surrounding
            #vertically and horizontally adjacent locations

            dfs(row+1,col)
            dfs(row,col+1)
            dfs(row-1,col)
            dfs(row,col-1)

            return
            




        for row in range(len_row):
            for col in range(len_col):
                #we dont care if its a 0
                #we want to check if it is a 1, then check if its connected
                #to vertically or horizontally connected nodes
                key=tuple([row,col])
                if grid[row][col]=='1' and key not in seen:
                    #have a dfs function that explores surrounding nodes
                    dfs(row,col)
                    print(seen)
                    self.number_of_islands+=1
        return self.number_of_islands