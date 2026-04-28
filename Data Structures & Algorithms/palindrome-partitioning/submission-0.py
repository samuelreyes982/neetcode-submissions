class Solution:
    def partition(self, s: str) -> List[List[str]]:
        combination_array=list(s)
        seen=set()
        result=[]


        def dfs(i,substring):
            
            if i >len(s):
                return

            
            if i ==len(s):
                key=tuple(substring)

                if key in seen:
                    return
                
                
                seen.add(key)
                result.append(substring[:])
                return
            
            
            #todo understand this crap
            for j in range(i, len(s)):
                piece = s[i:j+1]
                if is_palindrome(piece):
                    substring.append(piece)
                    dfs(j + 1, substring)
                    substring.pop()



    



        def is_palindrome(s):
            l=0
            r=len(s)-1

            while l<r:
                if s[l]!=s[r]:
                    return False
                l=l+1
                r=r-1
            return True                
        dummy =[]
        dfs(0,dummy)
        return result