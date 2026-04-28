class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        
        
        dp={}
        dp[0]=nums[0]
        


        for i in range(1,len(nums)-1):
            
            
            
            copy=dp.copy()
            del copy[i-1]
            
            if len(copy)>0:
                dp[i]= max(copy.values())+nums[i]
            else:
                dp[i]=nums[i]
            
        print(dp)  

        dp2={}
        dp2[1]=nums[1]
        

        
        for i in range(2,len(nums)):
            
            
            
            copy=dp2.copy()
            
            del copy[i-1]
            if len(copy)>0:
                dp2[i]= max(copy.values())+nums[i]
            else:
                dp2[i]=nums[i]
        print(dp2)
        first_max=max(dp.values())
        second_max=max(dp2.values())
        return max(first_max,second_max)
       
        