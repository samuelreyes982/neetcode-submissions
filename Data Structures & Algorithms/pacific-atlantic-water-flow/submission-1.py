class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        len_row=len(heights)

        len_col = len(heights[0])


        pacific=set()
        atlantic=set()


        def dfs(row,col,ocean,prev):
            key=tuple([row,col])
            if key in ocean:
                return
            #check bounds
            if row<0 or row>len_row-1 or col<0 or col>len_col-1:
                return
            
            
            prev_row,prev_col=prev

            
            if heights[row][col]>=heights[prev_row][prev_col]:
                print(f'point {row} {col}: prev point:{prev_row} {prev_col}')
                ocean.add(key)
                dfs(row+1,col,ocean,[row,col])
                dfs(row-1,col,ocean,[row,col])
                dfs(row,col+1,ocean,[row,col])
                dfs(row,col-1,ocean,[row,col])
            else:
                return
                
            
            
            
            

        #we need to add all elements in row 0 or col 0 to pacific since they are adj

        #we also need to add all elements in last row or last to atlantic



        for row in range(len_row):
            for col in range(len_col):
                if row==0 or col==0:
                    #pacific.add(tuple([row,col]))
                    dfs(row,col,pacific,[row,col])
                if row==len_row-1 or col==len_col-1:
                    #atlantic.add(tuple([row,col]))
                    dfs(row,col,atlantic,[row,col])

        #now that we have all adj nodes we need to
        result=[]
        for row in range(len_row):
            for col in range(len_col):
                key=tuple([row,col])
                if key in pacific and key in atlantic:
                    result.append([row,col])

        return result




        