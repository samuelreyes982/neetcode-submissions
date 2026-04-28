class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp={}
        #we know that dp[0]=0 eg, there are 0 ways to reach 0 steps with step size 1 or 2
        dp[0]=0
        dp[1]=1
        dp[2]=2
        #for every way we can reach an even number we can add another way using 2
        for i in range(3,n+1,1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]