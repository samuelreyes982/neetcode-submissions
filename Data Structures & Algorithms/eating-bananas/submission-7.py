class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''
        we are searching for min k 

        such that 


        [sum(element/k for all items in piles)>h ]
        if we are guarenteed a solution

        such that we can eat all piles in h hours

        if h==(len(nums)) then k = max(nums)

        in our worst case, k=max element in array, but it can 
        potentially be smaller but we know that it wont be bigger

        in our search for k

        k is between 0-max(element)

        we can use binary search to find our element
        between 0 and max element



        '''

        k=max(piles)
        piles=sorted(piles)
        left=1
        right=k
        while left<=right:
            print(f'left {left}. right {right}')
            middle=(left+right)//2

            #we should check if it satisfies our condition
            summ=0
            for i in range(len(piles)):
                calculation=piles[i]/middle
                if calculation>0 and calculation <1:
                    summ+=1
                elif calculation > int(calculation):
                    summ+=int(calculation)+1
                elif calculation == int(calculation):
                    summ+=calculation

            if summ<=h:
                #we found a potential k
                #print(f'summ {summ}. piles[middle] : {piles[middle]}')

                k=min(middle,k)
                right=middle-1
            elif summ>h:
                left=middle+1
            
        return k
                










        