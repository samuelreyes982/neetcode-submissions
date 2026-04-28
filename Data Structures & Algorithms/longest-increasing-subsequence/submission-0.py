class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        #lets try and do a dfs, then we can try and memoize it 

        
        
        def dfs(i,len_path):
            print(f'i: {i}, nums[i]: {nums[i]}   len_path: {len_path}')
            if i == len(nums)-1:
                #check length of increasing sequnce then kill recursion
                self.max_sequence=max(len_path,self.max_sequence)
                return
            j=i+1
            while j <=len(nums)-1:
                if nums[i]<nums[j]:
                    dfs(j,len_path+1)
                j=j+1
            #if this doesnt complete, we could not find a larger value so our path ends here
            #check length then stop
            self.max_sequence=max(len_path,self.max_sequence)
            return

        self.max_sequence=0
        for i in range(len(nums)):
            dfs(i,1)
        return self.max_sequence
            


        