class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res=[]
        seen=set()



        #recurse over and return all different combinations using dfs for decision tree

        def dfs(substring):

            #base case, we want to stop recursing when we go over sum, aka too large
            if sum(substring)>target:
                #no more recursing we want to call it quits
                return
            #we have found a potential combination, if it is unique and we havent seen it before
            key=tuple(sorted(substring))

            if sum(substring)==target and key not in seen:
                #we found a combination
                res.append(substring)
                seen.add(key)

            #else we have substring that is still lower then target and hasnt went over


            for canidate in nums:
                temp=substring.copy()
                temp.append(canidate)
                dfs(temp)
            return
        dfs([])
        return res 
                


        