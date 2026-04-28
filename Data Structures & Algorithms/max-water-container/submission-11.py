class Solution:
    def maxArea(self, heights: List[int]) -> int:

        nums=heights
        maxx=0

        left=0
        right=len(heights)-1


        while left<right:
            #calculate our area
            #we are bottlenecked by our smaller value
            smaller=min(nums[left],nums[right])

            length=right-left

            area=length*smaller
            #comparing our computed area, with last known max
            maxx=max(area,maxx)

            #update our pointers so that we can check
            #every viable solution

            #since we are being bottlenecked by our smaller value, we 
            #can search for a potential better value that might increase
            #our max area, we shift smaller one 

            if nums[left]>nums[right]:
                right=right-1
            elif nums[right]>nums[left]:
                left=left+1
            else:
                left+=1
                right-=1
        return maxx


        