class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # we are going to recurse for every 
        #item in nums, and do a two pointer to the right of it until we find a value 
        #that equals target or until right=left

        nums=sorted(nums)
        result=[]
        seen=set()
        for element in range(len(nums)):
            #we are gonna do 2 sum on the right side of the array from every element in list
            left=element+1
            right=len(nums)-1

            while left<right:
                summ=nums[element]+nums[left]+nums[right]

                if summ >0:
                    right-=1
                elif summ<0:
                    left+=1
                else:
                    
                    key=tuple(sorted([nums[element],nums[left],nums[right]]))
                    if key not in seen:
                        result.append([nums[element],nums[left],nums[right]])
                        seen.add(key)
                    left+=1
        return result



        