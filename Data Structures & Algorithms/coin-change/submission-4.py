class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[None]*(amount+1)
        
        dp[0]=0

        for i in range(1,amount+1):
            minn=float('inf')
            for coin in coins:
                if coin<i:
                    if dp[i-coin]!= None:
                        minn=min(minn,dp[i-coin]+1)
                        dp[i]=minn
                if coin ==i:
                    minn=min(minn,1)
                    dp[i]=minn
        print(dp)
        if dp[amount]==None:
            return -1
        else:
            return dp[amount]
