class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_rows=len(board)
        len_cols=len(board[0])

        self.found=False
        seen=set()



        def dfs(row,col,index,substring):
            print(f'substring :{substring}   word: {word[:index+1]}')
            print(f'row: {row} col: {col}')
            key=tuple([row,col])

            if row>len_rows-1 or row<0 or col>len_cols-1 or col<0 or key in seen:
                return
            
            
            #seen.add(key)
            temp=substring
            temp+=board[row][col]
            if substring!=word[:index+1]:
                print('bad substring')
                return 
            if temp== word:
                self.found=True
                return 
            seen.add(key)
            dfs(row+1,col,index+1,temp)
            dfs(row-1,col,index+1,temp)
            dfs(row,col+1,index+1,temp)
            dfs(row,col-1,index+1,temp)
            
            #make sure to remove key after path 
            #make sure to remove key after recursive calls for word search
            #make sure to remove key after recursive calls for word search
            seen.remove(key)
            return








        for row in range(len_rows):
            for col in range(len_cols):
                if board[row][col]==word[0]:
                    print(f'row {row} col {col} word[0]{word[0]}')
                    dfs(row,col,-1,'')
                    #reset seen
                    seen=set()
        return self.found
