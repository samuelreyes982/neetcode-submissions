class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        '''

        plan is to use one number as the center, 
        then we use a closing window to optimize
        lets just try and find a naive solution first then
        we can go about improving efficiency
        '''
        nums=sorted(nums)
        results=[]
        seen=set()
        for num in range(len(nums)):
            mid=num
            right=len(nums)-1
            left=0

            while left<right:
                
                summ=nums[mid]+nums[right]+nums[left]
                #print(f'left {left}. mid {mid}. right {right}. summ {summ}')
                if  summ==0:
                    if mid != right and mid !=left and left!=right:
                        sort=sorted([nums[left],nums[mid],nums[right]])
                        key=tuple(sort)
                        if key not in seen:
                            results.append(sort)
                            seen.add(key)
                    #not sure what to do if we have a match but its the same keys                   
                    left+=1
                elif summ <0:
                    left+=1
                else:
                    right-=1
        return results