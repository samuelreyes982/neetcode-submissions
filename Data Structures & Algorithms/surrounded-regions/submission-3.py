class Solution:
    def solve(self, board: List[List[str]]) -> None:
        len_row=len(board)
        len_col=len(board[0])
        seen=set()
       
        def dfs(row,col):
            if row>len_row-1 or row<0 or col>len_col-1 or col<0:
                return

            if board[row][col]!='O':
                return
       
            if board[row][col]=='O':
                board[row][col]='T'

            #recurse over neighbors
            dfs(row+1,col)  
            dfs(row-1,col) 
            dfs(row,col-1) 
            dfs(row,col+1)   
       # step 1.) get all border o and turn them into T

        



        for row in range(len_row):
            for col in range(len_col):
                boarders=[0,len_row]
                if row == 0 or row ==len_row-1 or col ==0 or col==len_col-1:
                    if board[row][col]=='O':
                        dfs(row,col)
        #step 2.) turn all inside o into x
        # step 1.) get all border o and turn them into T

        for row in range(len_row):
            for col in range(len_col):
                if board[row][col]=='O':
                    board[row][col]='X'
        

        #step 3.) turn all boarder t back into o
        for row in range(len_row):
            for col in range(len_col):
                if board[row][col]=='T':
                    board[row][col]='O'
        '''
        board=[["O","X","X","O","X"],
               ["X","O","O","X","O"],
               ["X","O","X","O","X"],
               ["O","X","O","O","O"],
               ["X","X","O","X","O"]]
        '''
        