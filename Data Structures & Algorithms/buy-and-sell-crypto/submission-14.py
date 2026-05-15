class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left=0
        right=1
        max_profit=0
        while right<len(prices):
            local_profit=prices[right]-prices[left]
            if local_profit>0:
                max_profit=max(local_profit,max_profit)
            if prices[right]<prices[left]:
                left=right
                right=right+1
            else:

                right+=1
        return max_profit
        