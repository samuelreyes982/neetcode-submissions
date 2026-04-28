class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        product=1
        zero=0
        for x in nums:
            if x!=0:
        
                product*=x
            else:
                zero+=1
        
        for i in range(len(nums)):
            if zero>1:
                nums[i]=0
            elif zero==1 and nums[i]!=0:
                nums[i]=0
            elif zero==1 and nums[i]==0:
                nums[i]=product
            elif product!=0:
                nums[i]=product//nums[i]
        return nums