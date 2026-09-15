class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        result=0

        num_rows=len(grid)

        num_cols=len(grid[0])

        seen=set()


        def search(row,col):
            #condition #1.) valid row col, not out of bounds

            if row<0 or row>=num_rows:
                return
            if col<0 or col>=num_cols:
                return

            #condition #2.) have we seen this before
            key=tuple([row,col])
            if key in seen:
                return
            #condition #3.) is this '1' or not
            if grid[row][col]=='0':
                return

            #if we got this far we should
            # we have found an adjacent 1 keep searching
            
            #making sure we don't recurse over this anymore
            seen.add(key)

            search(row+1,col)#up
            search(row-1,col)#down
            search(row,col+1)#right
            search(row,col-1)#left

        for row in range(num_rows):
            for col in range(num_cols):
                key=tuple([row,col])
                if grid[row][col]=='1' and key not in seen:
                    search(row,col)
                    result+=1
        return result


        