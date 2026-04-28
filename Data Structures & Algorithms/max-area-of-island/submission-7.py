class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row_len=len(grid)
        col_len=len(grid[0])
        maxx=0
        seen=set()

        def dfs(row,col):
            #check boundaries
            if row<0 or row>row_len-1 or col<0 or col>col_len-1:
                #terminate call
                return 0
            #check if weve seen this cell before
            key=(row,col)
            if key in seen or grid[row][col]==0:
                return 0
            seen.add(key)

            return 1+ dfs(row+1,col)+ dfs(row,col+1)+dfs(row-1,col)+dfs(row,col-1)



        for row in range(row_len):
            for col in range(col_len):
                #find island 
                if grid[row][col]==1:
                    #now we need to find all connected components and find the area 
                    curr_area=dfs(row,col)
                    maxx=max(maxx,curr_area)
        return maxx