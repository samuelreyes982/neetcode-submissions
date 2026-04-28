class Solution:
    def solve(self, board: List[List[str]]) -> None:

        row_len=len(board)
        col_len=len(board[0])
        
        seen=set()
        def dfs(row,col):
            key=tuple([row,col])

            if key in seen or col<0 or col>col_len-1 or row<0 or row>row_len-1:
                return
            if board[row][col]!='O':
                return
            seen.add(key)

            board[row][col]='s'
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1) 

        
        
        
        
        
        
        
        #get boardering os 

        for row in range(row_len):
            for col in range(col_len):
                if row== 0 or row==row_len-1 or col==0 or col==col_len-1:
                    if board[row][col]=='O':
                        #switch
                        dfs(row,col)


        #turn all o's into x

        for row in range(row_len):
            for col in range(col_len):
                
                if board[row][col]=='O':
                    #switch
                    board[row][col]='X'
        #turn all s back into o
        for row in range(row_len):
            for col in range(col_len):
                
                if board[row][col]=='s':
                    #switch
                    board[row][col]='O'
            