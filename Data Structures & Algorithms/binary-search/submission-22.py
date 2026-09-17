class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        '''

        cutting our search in half everytime, basically if our mid point
        is less than or greater then, we make a new subsect of numbers 
        based on disgarding values that arent in our search space. tldr we are making a smaller 
        search space each pass
        '''

        right=len(nums)-1
        left=0
        mid=0



        while left<=right:
            #compute our mid
            mid=(left+right)//2
            print(f'left: {left}.    mid : {mid}.  right   {right}')
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                #we found target
                return mid
        # this runs out
        # no solution
        return -1