class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        were gonna use binary search to look through an array to 
        find a specific target

        however the list is rotated, but some parts are sorted, 
        but its like spliced up

        we want to find a specific target in (logn) time


        '''


        left=0
        right= len(nums)-1


        while left <= right:
            #first we need to figure out if were in left sorted or right sorted

            middle= (left+right)//2
            print(f'left {left} middle {middle} right {right}')
            print(f'numsleft: {nums[left]} numsmiddle: {nums[middle]} numsright: {nums[right]}')
            if target==nums[middle]:
                return middle

            #right side of sorted array
            if nums[middle] >= nums[left]:
               
                if target > nums[middle] or target < nums[left]:
                    #go right
                    left=middle+1
                else:
                    right = middle -1

            else:
                #middle > left

                if target< nums[middle] or target > nums[right]:
                    #go right
                    right=middle-1
                else:
                    left = middle +1

        return -1