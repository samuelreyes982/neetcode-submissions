class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        #brute force
        dp={}
        self.ways=0
        
        
        
        def dfs(i,summ):
            
            #base case to stop once we get to last index in list
            #print(f'i : {i}.    summ{summ}')
            if i>len(nums)-1:
                if summ==target:
                    return 1
                else:
                    return 0

            #memoize
            key=tuple([i,summ])
            if key in dp:
                return dp[key]

            
            summ_pos=summ+nums[i]
            

        

            summ_negative=summ-nums[i]
            dp[key]=(dfs(i+1,summ_pos)+ dfs(i+1,summ_negative))

            return dp[key]
            
            
        
        
        return dfs(0,0)

        
        