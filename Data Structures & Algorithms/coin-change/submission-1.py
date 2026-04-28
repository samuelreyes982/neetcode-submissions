class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        '''
        we are gonna implement the brute force dfs
        '''
        self.min_path=None
        memo={}
        def dfs(steps,target):
            
            if target<0:
                return


            if target==0:
                if self.min_path==None:
                    self.min_path=steps
                else:
                    self.min_path=min(self.min_path,steps)
                return
            if target in memo and steps >= memo[target]:
                return
            memo[target]=steps

            #recursive call all options
            for nums in coins:
                if self.min_path is not None and steps+1>=self.min_path:
                    continue
                dfs(steps+1,target-nums)
        dfs(0,amount)

        if self.min_path==None:
            return -1
        else:
            return self.min_path



        



        