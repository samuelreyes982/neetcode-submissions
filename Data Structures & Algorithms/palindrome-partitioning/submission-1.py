class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result=[]
        def is_pal(s):
            l=0
            right=len(s)-1
            while l<=right:
                if s[l]!=s[right]:
                    return False
                l+=1
                right-=1
            return True


        def dfs(substring,choices):
            print(f'substring {substring} choices: {choices}. len choice {len(choices)}')
            if len(choices)==0:
                result.append(substring)
                return



            for i in range(len(choices)):
                temp=substring.copy()

                temp.append(choices[:i+1])
                new_choices=choices[i+1:]
                
                if is_pal(choices[:i+1]):
                    dfs(temp,new_choices)
        dfs([],s)     
        return result       
            
        

        