class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_row=len(grid)
        len_col=len(grid[0])

        seen=set()
        self.max_cells=0


        def dfs(row,col):
            #set bounds
            if row<0 or row > len_row-1 or col <0 or col>len_col-1:
                #means out of bounds kill recursive call
                return 0
            key = tuple([row,col])

            if key in seen or grid[row][col]==0:
                #means weve already seen it or it isnt part of our island
                return 0
            #we want to add point to our set
            seen.add(key)
            #check around us, not counting diagonals
            #this gives us number of cells in island
            return (1+dfs(row+1,col)+dfs(row,col+1)+dfs(row-1,col)+dfs(row,col-1))








        for row in range(len_row):
            for col in range(len_col):
                key=tuple([row,col])
                if key not in seen and grid[row][col]==1:
                    #we need to recurse over all horizontal and vertically adjacnet nodes
                    #and calculate the number of nodes and mark them seen
                    computed_cell=dfs(row,col)
                    #updated our max to potential computed max
                    self.max_cells=max(computed_cell,self.max_cells)
        return self.max_cells


