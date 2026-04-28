class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        left=1
        right=max(piles)

        k=right
        #well we have a k that works but were trying to find then lowest k in
        #our len(piles) because k will equal one of the piles, but we can find 
        #k more effiecently with binary search
        #. [1,2,3,4]
        while left<=right:
            middle = (left+right)//2
            total=0
            for x in piles:
                total+=math.ceil(x/middle)


            #total number of hours
            if total<=h:
                k=min(k,middle)
                right=middle-1
            else:
                left=middle+1
        return k



        