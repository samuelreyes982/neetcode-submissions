import string
class Solution:
    def numDecodings(self, s: str) -> int:
        #we would have to make our map

        #set a cache with answers to the values

        dp={len(s) : 1}

        def dfs(i):
            #weve already computed the result in index i, so we can just
            #retrieve that from cache
            if i in dp:
                return dp[i]
            #if our start is 0 we cant decode since none start with 0
            if s[i]=="0":
                return 0
            # we can do single digit by single digit 
            res=dfs(i+1)

            if i +1 < len(s) and (s[i]=="1" or s[i]=="2" and s[i+1] in '0123456'):
                res+=dfs(i+2)
            dp[i]=res
            return res
        return dfs(0)



