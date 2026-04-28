class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ways=0
        
        
        
        def dfs(i,summ):
            
            #base case to stop once we get to last index in list
            #print(f'i : {i}.    summ{summ}')
            if i>len(nums)-1:
                if summ==target:
                    self.ways+=1
                return
            
            summ_pos=summ+nums[i]
            dfs(i+1,summ_pos)

            summ_negative=summ-nums[i]
            dfs(i+1,summ_negative)
            
            return
        
        
        dfs(0,0)

        return self.ways
        