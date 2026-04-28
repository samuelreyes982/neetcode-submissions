class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp=[False]*(len(s)+1)

        dp[len(s)]=True


        for i in range(len(s)-1,-1,-1):
            print(i)
            for word in wordDict:
                print(s[i: i+len(word)])
                if word==s[i:i+len(word)]:
                    print(s[i:])
                    print(f'len word = {len(word)}')
                    if dp[i+len(word)]==True:
                        print('true')
                        dp[i]=True
                       
                        
        print(dp)
        return dp[0]
