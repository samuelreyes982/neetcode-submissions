class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0

        left=0
        right=left+1
        while left<len(prices):
            
            # we found a profitable sale, keep going until it is unprofitable
            #then we see if it is our max profit
            while right<len(prices):
                curr_profit=prices[right]-prices[left]
                max_profit=max(max_profit,curr_profit)
                right+=1

            left+=1
            right=left+1
            
        return max_profit