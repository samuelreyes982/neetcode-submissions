class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp=[None]*(amount+1)
        dp[0]=0


        for i in range(1,amount+1):
            minn=float('inf')
            for coin in coins:
                if coin<=i:
                    minn=min(1+dp[i-coin],minn)
            dp[i]=minn
        print(dp)
        if dp[amount] ==float('inf'):
            return -1
        else:
            return dp[amount]

        