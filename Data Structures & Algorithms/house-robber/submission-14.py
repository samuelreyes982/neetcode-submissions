class Solution:
    def rob(self, nums: List[int]) -> int:

        '''
        seems like i can either do +2 or +3
        because i cant do plus one so i gotta figure which one is better


        
        '''
        #edge case

        if len(nums)==1:
            return nums[0]
        
        
        dp=[None]*len(nums)

        dp[len(nums)-1]=nums[-1]
        dp[len(nums)-2]=nums[-2]

        
        for x in range(len(nums)-3,-1,-1):
            #print(x)
            #check from start up till one in front
            maxx_list=[]
            for path in range(len(nums)-1,x+1,-1):
                #print(path)
                maxx_list.append(dp[path])
            dp[x]=nums[x]+max(maxx_list)
        return max(dp)
