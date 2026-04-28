class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp=[0]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            maxx=1
            for j in range(i,len(nums)):
                print(f'i {i}. j {j}')
                if nums[j]>nums[i]:
                    maxx=max(maxx,1+dp[j])
            dp[i]=maxx
        print(dp)
        return max(dp)

        