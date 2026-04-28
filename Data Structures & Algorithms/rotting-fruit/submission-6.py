class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        '''
        well we first want to go through all locations in our graph, and we count the number of 
        fresh oranges and then we want to add all of the rotten oranges to our queue

        then once we do that we will for each rotton node in our bfs, we will infect all oranges 
        and then we will decrement the number of fresh oranges

        if all fresh oranges = 0 we return the time it took 

        if not we return negative one because a solution to make all oranges rotten does not exist

        '''
        # as we start all graph problems lets set up our data structures and variables
        len_rows=len(grid)
        len_cols=len(grid[0])
        queue=collections.deque()
        fresh_oranges=0
        time=0



        #lets iterate over all points

        for row in range(len_rows):
            for col in range(len_cols):
                if grid[row][col]==1:
                    fresh_oranges+=1
                elif grid[row][col]==2:
                    queue.append([row,col])



        while queue and fresh_oranges>0:
            print(f'level of rotten oranges: {queue}')
            for _ in range(len(queue)):
                row,col=queue.popleft()

                if row+1 <=len_rows-1:
                    if grid[row+1][col]==1:
                        queue.append([row+1,col])
                        grid[row+1][col]=2
                        fresh_oranges-=1

                if row-1 >=0:
                    if grid[row-1][col]==1:
                        queue.append([row-1,col])
                        grid[row-1][col]=2
                        fresh_oranges-=1

                if col-1 >=0:
                    if grid[row][col-1]==1:
                        queue.append([row,col-1])
                        grid[row][col-1]=2
                        fresh_oranges-=1
                
                if col+1 <=len_cols-1:
                    if grid[row][col+1]==1:
                        queue.append([row,col+1])
                        grid[row][col+1]=2
                        fresh_oranges-=1
            time+=1
        print(f'fresh_oranges:    {fresh_oranges} time: {time}')
        


        
        if fresh_oranges==0:
            return time
        else:
            return -1