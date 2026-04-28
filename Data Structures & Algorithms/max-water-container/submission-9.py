class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_water=0

        left=0
        right=len(heights)-1

        while left<right:
            print(f'left: {left}   right: {right}   ')
            lowest_bar=min(heights[left],heights[right])
            level=lowest_bar*(right-left)
            max_water = max(level,max_water)

            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
            
        return max_water

        