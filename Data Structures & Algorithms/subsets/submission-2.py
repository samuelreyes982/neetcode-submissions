class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res=[]

        seen=set()


        def dfs(i,substring):
            key=tuple(sorted(substring))
            if key in seen :
                return
            
            if i == len(nums):
                res.append(substring)
                seen.add(key)
                return                


            
            #include
            new=substring.copy()
            new.append(nums[i])
            dfs(i+1,new)

            #exclude
            new2=substring.copy()
            dfs(i+1,new2)


            return
        dfs(0,[])
        return res

