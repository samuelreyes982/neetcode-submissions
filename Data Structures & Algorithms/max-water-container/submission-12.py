class Solution:
    def maxArea(self, heights: List[int]) -> int:


        max_water=0


        left=0
        right=len(heights)-1


        while left<right:
            
            width=(right-left)
            computed=width*min(heights[left],heights[right])
            #print(f'left {left}. right { right} computed {computed} width {width}')

            max_water=max(computed,max_water)

            if heights[left]>heights[right]:
                right-=1
            
            elif heights[left]<=heights[right]:
                left+=1
        return max_water