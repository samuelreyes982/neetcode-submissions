class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        
        
        grid=[]
        #create a grid
        for i in range(m):
            grid.append([0]*(n))

        #set our end spot to 1
        grid[m-1][n-1]=1
        print(grid)


        #now lets iterate over every row and column backwards from end point which equals 1
        # OUR algorithm is that our new grid[row][col]= grid[row+1][col] grid[row][col+1]
        # if any point out of bounds of grid, consider it having a value of 0.

        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                #so we dont change end
                if grid[row][col]==0:
                    if row+1>m-1:
                        under=0
                    else:
                        under=grid[row+1][col]
                    if col+1>n-1:
                        right=0
                    else:
                        right=grid[row][col+1]
                    grid[row][col]=right+under
                    



        return grid[0][0]

        