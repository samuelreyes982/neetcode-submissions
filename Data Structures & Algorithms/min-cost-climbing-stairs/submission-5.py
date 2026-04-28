class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost))

        dp[len(cost)-1]=cost[-1]
        dp[len(cost)-2]=cost[-2]

        #traverse backwards
        for i in range(len(cost)-3,-1,-1):
            print(f'dp: {dp}')
            dp[i]=min(dp[i+1],dp[i+2])+cost[i]

        return min(dp[0],dp[1])