class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_len=len(grid)
        col_len=len(grid[0])
        islands=0
        seen=set()
        #search adjacent rows and cols
        def dfs(row,col):
            #boundary check
            if row<0 or row>row_len-1 or col<0 or col>col_len-1:
                #bad call terminate recursion
                return
            
            #check if weve passed over cell yet
            key=(row,col)
            if key in seen:
                return

            #so in bound not in seen and equals 1, we mark it and check its adjacent cells
            if grid[row][col]=='1':
                seen.add(key)
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)
            

        for row in range(row_len):
            for col in range(col_len):
                print(f'row: {row}. col: {col}')
                if grid[row][col]=='1' and (row,col) not in seen:
                    
                    dfs(row,col)
                    #after seeing how big the island and marking
                    #all correct sells we finally increment number of islands
                    islands+=1
                    
                    
        return islands  
    '''
    [["1","1","0","0","1"]
    ["1","1","0","0","1"]
    ["0","0","1","0","0"]
    ["0","0","0","1","1"]]
    '''    
