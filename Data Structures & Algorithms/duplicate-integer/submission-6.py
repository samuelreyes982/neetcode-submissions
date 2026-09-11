class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dic={}

        for x in nums:
            #print(dic.keys())
            if x not in dic.keys():
                dic[x]=1
            else:
                return True
        return False


            