class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        '''
        so we have an upper bound of the the largest k

        max(piles) is the largest k possible if we want to get it done 
        in h hours where h is len(piles)

        we need to find the smallest k possible so the smallest number

        between 1 and max(piles) that satisfies our condition


        we can reduce the search space if we use binary search
        '''


        

        left=1
        right=max(piles)
        min_k=right
        
        while left<=right:
            mid=(left+right)//2
            print(f'left : {left}.  mid: {mid}.  right {right}')
            
            #check condition
            total_hours=0
            for item in piles:
                
                #may need revision test
                total_hours+=(math.ceil(item/mid))
            
            if total_hours<=h:
                #valid k
                min_k=min(min_k,mid)
                right=mid-1
            else:
                #to small
                left=mid+1
        return min_k

        