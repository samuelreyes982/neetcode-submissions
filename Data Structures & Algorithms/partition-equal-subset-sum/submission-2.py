class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        summ=sum(nums)

        half_sum=summ/2

        if half_sum>int(half_sum):
            return False

        print(half_sum)

        #now that we have our target half sum, 
        #lets see if we can sum up to half sum with the elements in
        #array
        dp=[False]*(int(half_sum)+1)
        dp[0]=True
        
        for num in nums:
            for j in range(int(half_sum),num-1,-1):
                dp[j]= dp[j] or dp[j-num]


        return dp[int(half_sum)]

        