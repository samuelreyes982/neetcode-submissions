class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        plan is that we will use binary search which is O(log(n)) time complexity


        '''

        left=0
        right=len(nums)-1

        minn=float('inf')
        if len(nums)<=1:
            return nums[0]
        while left<right:
            
            #sorted
            if nums[left]<nums[right]:
                minn=min(minn,nums[left])
                
                break
            
            
            
            mid=(left+right)//2

            if nums[mid] > nums[right]:
                left=mid+1
                minn=min(minn,nums[right])
                print(nums[mid])
            elif nums[mid]<nums[right]:
                right=mid-1
                minn=min(minn,nums[mid])
            
            
        
        
        
        
        return minn


        