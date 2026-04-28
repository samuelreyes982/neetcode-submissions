class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        right=1
        left=0
        max_profit=0
        while right<len(prices):
            if prices[left]<prices[right]:
                max_profit=max(max_profit,prices[right]- prices[left])
            else:
                left=right
                
            right=right+1
        return max_profit



        