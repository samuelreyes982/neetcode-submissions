class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        len_rows=len(board)
        len_cols=len(board[0])

        self.found=False
        seen=set()



        def dfs(row,col,index,substring,parts):
            if len(substring)>=100:
                print(f'substring :{substring}   word: {word[:index+1]}')
                print(f'row: {row} col: {col}')
                print(f'seen so far {parts}')
            if [0,3] in parts and [1,2] not in parts:
                print(f'substring :{substring}   word: {word[:index+1]}')
                print(f'row: {row} col: {col}')
                print(f'seen so far {parts}')

            key=[row,col]

            if key in parts:
                print('bad key')
                return

            if row>len_rows-1 or row<0 or col>len_cols-1 or col<0:
                print('bad bouunds')
                return
            temp=substring
            temp+=board[row][col]
            #print(f'temp: {temp} word[index] {word[:index+1]}')
            if temp!=word[:index+1]:
                print('bad substring')
                return 
            #print(f' {board[row][col]} added to substring')
            parts.append(key)
            #temp=substring
            #temp+=board[row][col]
            if temp== word:
                self.found=True
                return 
            new_parts=parts.copy()
            new_parts2=parts.copy()
            new_parts3=parts.copy()
            new_parts4=parts.copy()
            dfs(row+1,col,index+1,temp,new_parts)
            dfs(row-1,col,index+1,temp,new_parts2)
            dfs(row,col+1,index+1,temp,new_parts3)
            dfs(row,col-1,index+1,temp,new_parts4)
            return








        for row in range(len_rows):
            for col in range(len_cols):
                if board[row][col]==word[0]:
                    #print(f'row {row} col {col} word[0]{word[0]}')
                    dfs(row,col,0,'',[])
                    #reset seen
                    #seen=set()
        return self.found
