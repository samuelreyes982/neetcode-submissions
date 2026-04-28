import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        we need to finish within h hours, so that is the baseline, 
        and we need to atleast hit that margin

        in example there are the same number of elements, as number 
        per hours. 

        this means, we only have one hour for each pile

        which means we are bounded by the largest pile for k
        , because it needs to be finished in 1 hour.
        so no matter what worst case scenario k being set to the largest
        number in piles is our upper bound, then we need to search 
        lower then that to see if we can a smaller k.

        we can probably check each element, below that in order, 
        but if we use binary search, it can make it log(n) instead of
        n
        '''
        #worst case k that satisfies h
        k=max(piles)

        #now we must check from 1-k for a smaller k that satisfies h

        left=1
        right=k
        while left<=right:
            
            middle=(left+right)//2
            print(f'left {left} middle {middle} right {right}')
            if middle==0:
                break
            #now check if middle satisfies h
            sum_hours=0
            for item in piles:
                print(item)
                sum_hours+= math.ceil(item/middle )   
            
            if sum_hours<=h:
                k=min(k,middle)
                right=middle-1
            else:
                left=middle+1


        return k







