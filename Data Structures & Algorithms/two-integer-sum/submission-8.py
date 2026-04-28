class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        '''we go through every number in our nums list, and we check if we have 
        the target-number in our previous seen items, and if we do
        return true
        , if we don't, we end up returning false
        '''
        dic={}
        for i in range(0,len(nums),1):
            #key is value, value is index
            if target-nums[i] in dic.keys():
                return [dic[target-nums[i]],i]
            else:
                dic[nums[i]]=i


        