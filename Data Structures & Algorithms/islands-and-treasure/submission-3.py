class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #first lets set our bounds and initiate our data structures
        len_rows=len(grid)
        len_cols=len(grid[0])

        seen=set()
        
        #for bfs we will use a double ended queue
        #queue=deque()

        #helper function
        
        def bfs(start_r, start_c):
            q = deque([(start_r, start_c)])
            visited = set([(start_r, start_c)])   # per-search visited
            distance = 0

            while q:
                for _ in range(len(q)):           # process one “ring” = same distance
                    r, c = q.popleft()
                    print(f'node: {r, c}')

                    if grid[r][c] == 0:
                        return distance

                    # explore 4-neighbors from the CURRENT node
                    for nr, nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                        if 0 <= nr < len_rows and 0 <= nc < len_cols and (nr, nc) not in visited:
                            if grid[nr][nc]!=-1:
                                visited.add((nr, nc))
                                q.append((nr, nc))
                distance += 1

            return 2147483647
                





        
        #now lets loop over all elements
        for row in range(len_rows):
            for col in range(len_cols):
                #were interested if it is equal to a land value
                key=tuple([row,col])
                if key not in seen and grid[row][col]== 2147483647:
                    #call helper function to run bfs on it 
                    print(f'found a land cell at row{row} col:{col}')
                    temp = bfs(row,col)
                    grid[row][col]=temp
                    self.distance=0