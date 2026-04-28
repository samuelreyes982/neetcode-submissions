class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]

        seen=set()

        def dfs(substring,choices,opens,closes):
            print(substring)
            key=tuple(substring)
            if key in seen or len(substring)>n*2:
                return
            

            
            if len(substring)== n*2 and key not in seen and opens==closes:
                res.append(substring)
                seen.add(key)

            
            if closes>opens:
                return
            #else we have work to do

            temp=substring
            new_choices=choices.copy()
            #1.)we can close
            temp+=')'
            dfs(temp,new_choices,opens,closes+1)           
            #2.) add a new open
            temp2=substring
            temp2+='('
            dfs(temp2,new_choices,opens+1,closes)
        dfs('',[],0,0)
        return res