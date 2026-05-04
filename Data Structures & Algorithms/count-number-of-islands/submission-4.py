class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        num_row= len(grid)

        num_col=len(grid[0])
        self.num_islands=0
        seen=set()

        def dfs(row,col):
            #elimnate process if
            key = tuple([row,col])
            #1: weve seen it before
            #2: it is 0
            #3 bad boundaries
            if row>num_row-1 or row<0:
                return
            if col>num_col-1 or col<0:
                return
            if key in seen or grid[row][col]=='0':
                return
            
            #else we add it to seen, then check
            #surrounding islands

            seen.add(key)
            #self.num_islands+=1

            dfs(row, col-1)
            dfs(row, col+1)
            dfs(row+1, col)
            dfs(row-1, col)  






        for row in range(num_row):
            for col in range(num_col):
                key=tuple([row,col])
                if grid[row][col]=='1' and key not in seen:
                    dfs(row,col)
                    self.num_islands+=1
                    
        return self.num_islands



        