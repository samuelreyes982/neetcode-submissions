class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #define bounds
        row_length=len(board)
        col_length=len(board[0])

        word_arr=list(word)


        self.found=False


        def dfs(row,col,substring):
            
            #print(f'substring: {substring}     wordarr:{ word}' )
            print(f'position:   {row},{col}')
            if substring==word:
                print("found true !!!!")
                self.found=True
                return True
                
            #bounding base case check
            
            if self.found==True:
                return
            
            if row>=row_length or col>=col_length or row<0 or col <0 or board[row][col]=="#":
                return
            
            #word base case check

            if substring!=word[:len(substring)]:
                return 
            #todo optimize so that we can decide if a substring wont be our answer early on-
            
            
            
            
                
            

            #explore routes, we can go up, down, left, or right
            
            #up
            #print(f'row : {row}  column:  {col} max row len: {row_length}.    max col len:{col_length}')
            temp= str(board[row][col])
            board[row][col]="#"
            
            dfs(row,col+1,substring+temp)

            #down
            dfs(row,col-1,substring+temp)
            #left
            dfs(row-1,col,substring+temp)
            #right
            dfs(row+1,col,substring+temp)
            board[row][col]=temp
        
        for x in range(row_length):
            for y in range(col_length):
                dfs(x,y,"")
        return self.found