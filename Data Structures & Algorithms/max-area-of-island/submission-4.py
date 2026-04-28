class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        len_row=len(grid)
        len_col= len(grid[0])

        seen=set()
        max_area=0

        def dfs(row,col):

            key=tuple([row,col])

            if key in seen:
                return 0
            if row<0 or row > len_row-1 or col<0 or col>len_col-1 or grid[row][col]==0:
                return 0
            seen.add(key)
            return (1 + dfs(row+1,col)+ dfs(row-1,col)+dfs(row,col+1)+dfs(row,col-1))


        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col]==1:
                    temp=dfs(row,col)
                    max_area=max(max_area,temp)
        
        return max_area

