class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        seen=set()
        number_of_islands=0

        rows=len(grid)

        columns=len(grid[0])


        def dfs(row,col):
            #invalid call to evaluate row
            if row<0 or row>rows-1 or col<0 or col > columns-1 or tuple([row,col]) in seen:
                return
            if grid[row][col]=='0':
                return
            print(f'in dfs row {row}:  col {col}:')
            key=tuple([row,col])
            seen.add(key)

           
            dfs(row+1,col)
                        
            
            dfs(row-1,col)
                        
            
            dfs(row,col+1)
            
            dfs(row,col-1)

        '''
        1.) iterate over every edge in our graph
        since it is a 2d array we may need a double loop

        for 
            for

        2.) once we land on a edge when traversing our graph, 
            -if it is 0 we ignore
            -if it is a 1, we must figure out if it is an island or is it part of 
            an alr existing island
        
        3.) how to verify if it is alr in an island or not
            -check if it is already marked in seen
                if not we need to check if the nieghboring edges are in an island already
                we can check, up, down,left right, and if they are not marked,
                then we can increase island count, then mark current edge as island in seen
            
            if any of the nieghboring edges in seen, we then add to seen and return without
            adding a new island

        '''

        #1 double for loop
        for row in range(rows):
            for col in range(columns):
                print(f' looping over row: {row} col: {col}')
                key=tuple([row,col])
                print(f'val at row, col {grid[row][col]}')
                if grid[row][col]=='1' and key not in seen:
                    print(f'we found a 1 at ({row},{col})')
                    #check if nieghbors are in seen
                    #4 clunky if statememts
                    dfs(row,col)
                        #we have a 1 that is not part of an island
                        #we should add this to seen and we increase number of islands by 1 
                        
                    print(f'new island discovered at {key}')
                    number_of_islands+=1
                    
                 
                        # we have found a 1 where it has an adjacent edge that is an island, so we just mark it as seen
                            

                    

        return number_of_islands




        