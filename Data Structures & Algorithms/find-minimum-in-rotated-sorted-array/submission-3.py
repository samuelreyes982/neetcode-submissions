class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        considering we searching a sorted array for an min item
        and we want to achieve O(logn) time, this leads me to believe
        we are looking for a solution that utilizes binary search


        we can potentially have a normal sorted order like 
        [1,2,3,4,5,6]

        or we have it shifted potentially like
        [6,1,2,3,4,5]
        '''
        left=0
        right=len(nums)-1

        minn=float('inf')

        while left<=right:
            #weve calculated a potential minimum but we want to see if there is another smaller min
            middle=(left+right)//2
            minn=min(minn,nums[middle])
            
            print(f'nums[left]:{nums[left]}.  nums[right]{nums[right]}    nums[middle]: {nums[middle]}')
            # i think we find ourselves in 2 conditions
            #1.) we are either in the sorted portion
                #-left[nums]<right[nums]
            if nums[left]<nums[right]:
                right=middle-1
            #2.) we are in the rotated + sorted portion
                #left[nums]>right[nums]
            elif nums[left]>nums[right]:
                #if nums[middle]<nums[right]:
                left+=1
                
            else:
                left+=1
                right-=1
           
            




        return minn

        