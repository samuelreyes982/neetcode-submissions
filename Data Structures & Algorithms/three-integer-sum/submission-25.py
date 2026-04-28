class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        print(nums)
        result=[]
        nums_used_index=[]
        #iterating over every number to see if there are 2 numbers to make it 0
        seen=set()
        for item in range(len(nums)-1):

            left=item
            right=(len(nums)-1)
            middle=left+1
            while left<middle and middle <right:
                print(f'left {nums[left]} middle {nums[middle]}. right {nums[right]}')
                summ=nums[middle]+nums[right]+nums[left]
                if summ==0:
                    #result.append([nums[left],nums[middle],nums[right]])
                    key=tuple(sorted([nums[left],nums[middle],nums[right]]))
                    if key not in seen:
                        result.append([nums[left],nums[middle],nums[right]])
                        seen.add(key)
                    middle+=1
                    right-=1
                elif summ>0:
                    right-=1
                else:
                    middle+=1
        return result
