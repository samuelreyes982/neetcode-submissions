class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        #first things first, lets create our 2d array modeling this problem
        #columns=text1, and rows=text2
        
        grid=[]
        len_col=len(text1)
        len_row=len(text2)

        for i in range(len_row):
            grid.append([0]*len_col)


        #next lets start filling from the last cell up

        for row in range(len_row-1,-1,-1):
            for col in range(len_col-1,-1,-1):
                if row+1>len_row-1:
                    down=0
                else:
                    down= grid[row+1][col]

                if col+1>len_col-1:
                    right=0
                else:
                    right = grid[row][col+1]
                
                if text1[col]==text2[row]:
                    if row+1>len_row-1 or col+1 >len_col-1:
                        grid[row][col]=1
                    else:    
                        grid[row][col]=1 + grid[row+1][col+1]

                else:
                    grid[row][col]= max(right,down)



        return grid[0][0]

        