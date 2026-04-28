class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        '''
        i will basically deploy the subsets 1 algorithm and then add a set and check to see if the duplicates exist
        '''

        result=[]

        seen=set()


        def dfs(i,substring):

            if i == len(nums):
                key=tuple(sorted(substring))
                if key not in seen:
                    result.append(substring)
                    seen.add(key)
            
            if i>=len(nums):
                return

            #inclusive call
            dfs(i+1,substring+[nums[i]])



            #excluding call
            dfs(i+1,substring)        

        dfs(0,[])


        return result
        