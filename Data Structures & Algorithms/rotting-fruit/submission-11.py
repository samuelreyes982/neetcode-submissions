class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        len_row=len(grid)
        len_col=len(grid[0])
        seen=set()
        self.fresh_fruit=0
        q=collections.deque()
        def add(row,col):
            #bounds
            if row<0 or row>len_row-1 or col < 0 or col>len_col-1:
                return
            key=tuple([row,col])
            #if weve seen it or its not a fresh fruit
            if key in seen or grid[row][col]!=1:
                return
            #add fruit to queue
            #add to visited
            
            seen.add(key)
            q.append([row,col])
            grid[row][col]=2
            self.fresh_fruit-=1

            return
        
        #we are are gonna append all rotton fruits for our dfs
        for row in range(len_row):
            for col in range(len_col):
                #we are appending our rotten fruit to queue
                if grid[row][col]==2:
                    q.append([row,col])
                if grid[row][col]==1:
                    self.fresh_fruit+=1

        if self.fresh_fruit==0:
            return 0
        #now that weve appended all of our fruits, we are going to use bfs to 
        #search by levels from all rottenn fruits at the same time
        time=-1
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                #add all horizontaslly and vertically adjacent nodes to row,col
                add(row+1,col)
                add(row-1,col)
                add(row,col+1)
                add(row,col-1)
            time+=1


            
        print(grid)
        if self.fresh_fruit==0:
            return time
        else:
            return -1