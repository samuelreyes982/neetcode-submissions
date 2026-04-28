class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #default to catch any edge cases
        max_res=max(nums)
        
        min_val=1
        max_val=1

        #lets loop through all our elements once 
        for i in range(len(nums)):

            if nums[i]==0:
                min_val=1
                max_val=1
            else:

        #including max val, including min_val, start new subset
                temp=min_val
                min_val= min(max_val*nums[i],min_val*nums[i],nums[i])
            
            #do the same for max
                max_val=max(temp*nums[i],max_val*nums[i],nums[i])

                max_res=max(max_val,max_res)
        return max_res

        