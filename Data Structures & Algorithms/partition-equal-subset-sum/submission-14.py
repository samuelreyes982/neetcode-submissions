class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summ=sum(nums)/2

        if int(summ)<summ:
            return False
        summ=int(summ)
        dp=[False]*(summ+1)

        dp[0]=True

        for x in nums:
            for i in range(summ,x-1,-1):
                dp[i]=dp[i]or dp[i-x]
        print(dp)
        return dp[summ]
        