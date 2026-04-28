class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result=[]

        def backtrack(open_num,close_num,substring):

            #base case

            if open_num==close_num==n:
                
                result.append(substring)
                return
            

            #add open parenthesis if we arent at n
            
            #if open_num>closed_num
            if open_num<n:
                tmp=substring+"("
                backtrack(open_num+1,close_num,tmp)
            if close_num<open_num:
                tmp=substring+")"
                backtrack(open_num,close_num+1,tmp)

        backtrack(0,0,"")
        return result
            
        