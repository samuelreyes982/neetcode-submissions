class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        '''
        [1,2,3,target]
        [1]->->[3]->
        [2]->->
        '''
        dp={}
        dp[0]=cost[0]
        dp[1]=cost[1]

        #cost[len(cost)]=0
        for i in range(2,len(cost)+1):
            if i==len(cost):
                dp[i]=min(dp[i-1],dp[i-2])
            else:

                dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        print(dp)
        return dp[len(cost)]

        