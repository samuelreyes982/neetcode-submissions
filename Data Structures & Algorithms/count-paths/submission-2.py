class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        '''
        lets start at bottom left corner, and we basically make a bunch of different path calls
        and if it goes out of bounds we stop it, and if it succeeds in getting to our target we 
        count it

        ok so to optimize we are gonna use dynamic programming and create a grid where we use the number
        of paths from below and from the right calculate our value
        '''
        self.paths=0
        col=[0]*(n+1)
        grid=[]
        seen=set()
        for i in range(m+1):
            coll=col.copy()
            grid.append(coll)
        #print(grid)



        def search(row,col):
            #bounds
            
            if col<0 or col>=len(grid[0]):
                return

            if row<0 or row>=len(grid):
                return
            
            if row==0 and col==0:
                self.paths+=1
                return
            key=tuple([row,col])
            if key in seen:
                return
            seen.add(key)
            search(row-1,col)
            search(row,col-1)
            
            return





       

        grid[len(grid)-2][len(grid[0])-2]=1
        #print(grid)
        for row in range(len(grid)-2,-1,-1):
            for col in range(len(grid[0])-2,-1,-1):
                #print(f'row {row}.   col {col}')
                down=grid[row+1][col]
                right=grid[row][col+1]
                grid[row][col]=down+right+grid[row][col]
                #print(f'val : {grid[row][col]}')
        #print(grid)
        return grid[0][0]
        