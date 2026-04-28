class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid=[]
        
        for i in range(m):
            col=[0]*(n)
            grid.append(col)
        
        grid[m-1][n-1]=1
        
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                
                print(f'row {row} col {col}')
                if row+1>m-1:
                    bottom=0
                else:
                    bottom=grid[row+1][col]
                if col+1>n-1:
                    right=0
                else:
                    right=grid[row][col+1]
                
                grid[row][col]=bottom+right
                grid[m-1][n-1]=1
                




        print(grid)
        return grid[0][0]
        
        
        
       





        