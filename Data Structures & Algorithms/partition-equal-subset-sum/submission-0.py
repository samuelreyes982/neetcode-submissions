class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        '''
        if sum of all other elements is equal to our current comparator
        return true

        else keep comparing
        then return false

        seems like we can do a dynamic programming approach
        '''
        #we need half of the sum
        #check if it is an int



        if sum(nums)%2==1:
            return False
        half_sum=sum(nums)//2
        

        dp=[False]*(half_sum+1)
        print(f'half sum : {half_sum}')
        dp[0]=True
        for num in nums:
            for i in range(half_sum,num-1,-1):
                if dp[i-num]:
                    dp[i]=True
        

        print(f'dp:   {dp}')
        return dp[half_sum]


        