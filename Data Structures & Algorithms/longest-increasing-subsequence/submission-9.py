class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        dp[len(nums)-1]=1
        minn=nums[len(nums)-1]
        print(f'minn {minn}')
        for i in range(len(nums)-2,-1,-1):
            maxx=1
            for j in range(i+1,len(nums)):
                new=1+dp[j]
                if nums[i]<nums[j]:
                    if new>maxx:
                        maxx=new
            dp[i]=maxx

            

        print(dp)
        return max(dp)