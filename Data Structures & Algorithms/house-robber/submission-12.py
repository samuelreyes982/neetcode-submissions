class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        we can either start at 0

        or we can start at 1

        then we can either step 1 and rob that house or step 2 and rob that house
        
        i think at each step we can run max on the sum in order to calculate the max we 
        can get at each position until we reach the end
        '''
        
        if len(nums)==1:
            return nums[0]
        
        dp={}
        dp[0]=nums[0]
        dp[1]=nums[1]

        for i in range(2,len(nums)):
            # we can check any house that is behind our current house as 
            #long as its not adjacent
            new_dic=dp.copy()
            #essentially removing last adjacent node as a potential candidate

            del new_dic[i-1]

            largest_val=max(new_dic.values())



            dp[i]= largest_val+nums[i]
        
        print(dp)
        return max(dp[len(nums)-1],dp[len(nums)-2])
        