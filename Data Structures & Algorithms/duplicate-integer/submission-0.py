class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary={}
        for x in nums:
            if x in dictionary:
                return True
                

            else:
                dictionary[x]=x
            
        return False
