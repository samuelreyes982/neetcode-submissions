class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        '''
        trying a baxktracking sort of solution that tries all combinations 
        sort of like subsets problem
        
        we can reuse the same element more than once, but the same 3 numbers
        cant be used more than once, aka use set to verify triples
        '''
        nums.sort()

        return_string=[]

        seen=set()
        
        
        print(nums)
        
        for i in range(len(nums)):
            left=0
            right=len(nums)-1

            while left<right:
                sum=nums[left]+nums[right]+nums[i]
                if sum>0 or i==right:
                    right-=1
                elif sum<0 or i==left:
                    left+=1
                else:
                    print(f'left:   {nums[left]}    middle: {nums[i]}    right:{nums[right]} ')
                    if sum==0 and i != right and i !=left:
                        key=tuple(sorted([nums[left],nums[right],nums[i]]))
                        if key not in seen:
                            seen.add(key)
                            return_string.append([nums[left],nums[right],nums[i]])
                    left+=1
                    right-=1


            





        return return_string     
