class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left=0
        right=len(nums)-1
        print("started")

        while right>=left:
          
            
            middle=(right+left)//2
            print(f" right {right}.  middle {middle}.   left {left}")
            
            
            if nums[middle]==target:
                return middle
            elif nums[right]==target:
                return right
            elif nums[left]==target:
                return left
            
            elif middle== target or middle == left:
                return -1
            elif nums[middle]>target:
                right=middle
            else:
                left=middle
        return -1
        
        '''
        left=0 right=5.  middle=2 nums[middle]=2
        '''