class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q=collections.deque()

        len_rows=len(grid)
        len_cols=len(grid[0])
        seen=set()
        #add all chests to queue
        for row in range(len_rows):
            for col in range(len_cols):
                if grid[row][col]==0:
                    q.append([row,col])
        
        
        
        def add(row,col):
            #bounds
            if row>len_rows-1 or row<0 or col>len_cols-1 or col<0:
                return
            key=tuple([row,col])

            if key in seen or grid[row][col]==-1:
                return
            seen.add(key)
            q.append([row,col])
        
        
        
        
        #now do bfs on queue to find closest land values in levels
        
        level=0
        while q:

            for i in range(len(q)):
                row,col=q.popleft()
                if grid[row][col]==2147483647:
                    grid[row][col]=level
            
                #add all things around
                add(row+1,col)
                add(row-1,col)
                add(row,col+1)
                add(row,col-1)
            level+=1


        