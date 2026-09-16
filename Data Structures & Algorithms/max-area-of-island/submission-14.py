class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        '''

        so we are gonna search the whole grid, every row and column
        
        once we find an island, we figure out how big it is
        mark it as seen, then we compare it to our max which will start as 0

        then return max
        '''

        self.maxx=0

        row_length=len(grid)

        col_length=len(grid[0])
        seen=set()

        #recursive search col

        def search(row,col):
            #make sure we are within our bounds
            if row<0 or row >= row_length:
                return 0           
            if col<0 or col >= col_length:
                return 0           

            #or if weve seen it
            key=tuple([row,col])
            if key in seen or grid[row][col]==0:
                return 0
            
            #add
            seen.add(key)


            #search all adjacents
            return 1+ (search(row+1,col) +
            search(row-1,col)+
            search(row,col+1)+
            search(row,col-1))



        for row in range(row_length):
            for col in range(col_length):
                #check if weve seen
                key=tuple([row,col])
                if key not in seen and grid[row][col]==1:
                    self.maxx=max(search(row,col),self.maxx)
        return self.maxx
