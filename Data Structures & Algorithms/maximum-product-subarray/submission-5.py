class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxp=float('-inf')
        maxx=1
        minn=1


        for x in nums:
            temp=maxx
            maxx= max(x*maxx,x*minn,x)
            minn=min(x*temp,x*minn,x)

            maxp=max(minn,maxx,maxp)
        return maxp