class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        

        #basically 2 different starts

        #we can jump 1 or 2 spaces ahead

        #need to find cheapest path

        #we dont really know from the start which starting point
        '''
        will be cheaper, so we can start from the end and 
        iterate backwards
        well start at len(cost)+1
        '''

        dp=[None]*(len(cost)+1)

        #setting values
        dp[-1]=0
        dp[-2]=cost[-1]

        #loop from second to last all the way to 0 index
        for i in range(len(cost)-2,-1,-1):
            
            dp[i]= min(dp[i+1],dp[i+2]) + cost[i]
        

        print(dp)

        

        return min(dp[0],dp[1])
        



