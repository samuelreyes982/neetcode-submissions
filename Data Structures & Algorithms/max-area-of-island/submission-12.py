class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_island=0

        seen=set()

        row_len= len(grid)
        col_len=len(grid[0])

        def search(row,col):
            #before we search make sure we want to check

            #boundaries
            if row<0 or row>row_len-1 or col <0 or col>col_len-1:
                #not valid 
                return 0
            #have we checked it before or cell value is 0
            key=tuple([row,col])
            if key in seen or grid[row][col]==0:
                return 0

            #we need to check cell, and adjacent cells around it

            seen.add(key)

           # print(f'cell added row:{row}.   col:  {col}')
            
            return 1+search(row+1,col)+search(row-1,col)+search(row,col+1)+search(row,col-1)

        #to be continued
        for row in range(row_len):
            for col in range(col_len):
                local_max=0
                key=tuple([row,col])
                if grid[row][col]==1 and key not in seen :
                    local_max=search(row,col)
                    self.max_island=max(self.max_island,local_max)
        
        return self.max_island
        