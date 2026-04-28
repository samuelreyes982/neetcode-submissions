class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''

        binary search is a algorithm that basically has a left and right pointer , 
        and you are searching for a specific value in an ordered list.
        the part where it saves you time is that it halves the amount of options 
        you have each time, so that you have a reduced number of canadites you have to go through
        
        to put it simply you find the half point between your left and right
        then if the mid is lower then the value your searching for mid becomes left

        if mid is higher then the target, right pointer becomes mid

        you keep on updating pointers till you exhaust options or you find it
        
        '''

        right=len(nums)-1
        left=0
        
        while left<=right:
            
            #special cases
            if (right-left)<2:
                if nums[right]==target:
                    return right
                if nums[left]==target:
                    return left
                break

            #############
            mid=(left+right)//2
            print(f'left:{nums[left]} mid:{nums[mid]} right: {nums[right]}')
            #see if we got our target
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid
            elif nums[mid]<target:
                left=mid
            
        return -1
        