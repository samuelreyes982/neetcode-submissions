class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        sliding window is a way to optimize linear data structures that require contigiuos 
        updating

        1.) as we go through the list we want to update left if we find a 
        smaller value as it would be unprofitable

        2.) we are gonna have a window of values, and try and start at the lowest
        and end at the highest profitble point

        if we are still profitble lets compare to our max profit and if its bigger
        replace it 
        '''
        max_profit=0


        #starting point
        left=0
        right=1


        while right<len(prices):
            #check if profitable

            if prices[left]<prices[right]:
                print(f'right: {right}. left: {left}.  profit : {prices[right]-prices[left]}')
                max_profit=max(prices[right]-prices[left], max_profit)
                right+=1

            else:
                left=right
                right+=1

        return max_profit



        

