class Solution:
    def canPartition(self, nums: List[int]) -> bool:


        summ=sum(nums)/2

        if int(summ)<summ:
            return False
        summ=int(summ)
        dp=[False]*(summ+1)


        dp[0]=True
        print(dp)
        for x in nums:
            #backwards for single use knapsack
            for i in range(summ,x-1,-1):
                print(f'i :{i}.  x: {x} dp[i-x]. {dp[i-x]}')
                dp[i]= dp[i-x] or dp[i]

        print(dp)
        return dp[summ]
        