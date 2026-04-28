class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],'5':['l','k','j'],'6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],
        '9':['w','x','y','z']}
        results=[]
        seen = set()

        if not digits:
            return results
        def dfs(i,substring):

            if i == len(digits):
                results.append(''.join(substring))
                return
            
            for ch in dic[digits[i]]:
                substring.append(ch)
                dfs(i+1,substring)
                substring.pop()
        dfs(0,[])
        return results    
