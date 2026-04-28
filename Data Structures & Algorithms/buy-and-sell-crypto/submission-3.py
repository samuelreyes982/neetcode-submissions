class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1

        max=0

        while right<=len(prices)-1:
            #case where we want to move pointers because it is a total loss
            if prices[right] < prices[left]:
                left=right
                right=right+1
            #case where there is a potential gain and we keep going
            else:
                gain=prices[right]-prices[left]

                if gain > max:
                    max=gain
                right= right +1
        return max