class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        dic={}

        for x in range(len(nums)):
            if target-nums[x] in dic:
                return [dic[target-nums[x]],x]
            dic[nums[x]]=x
        
                