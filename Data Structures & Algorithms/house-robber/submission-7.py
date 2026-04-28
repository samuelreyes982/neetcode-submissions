class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1=0
        rob2=0

        n=len(nums) 


        for x in nums:
            new_rob=max(rob1+x,rob2)
            rob1=rob2
            rob2=new_rob
        return rob2
        