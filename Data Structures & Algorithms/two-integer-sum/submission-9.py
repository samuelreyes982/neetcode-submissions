class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}

        for i in range(len(nums)):
            
            print(f'i: {i}     nums[i]: {nums[i]}')
            print(f'dic {dic}')
            
            if target-nums[i] in dic:
                return [dic[target-nums[i]], i]
            else:
                dic[nums[i]]= i

    

        