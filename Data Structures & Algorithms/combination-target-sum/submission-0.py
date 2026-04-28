class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        maybe we can kinda use a similar algorithm that was used for subsets, but instead of using an index, we can just reuse the same 
        array over and over again but we can use the same logic of the decision to include or exclude, but instead of stopping because of reaching
        end index, we stop when our combination sum is greater then the targeet or == our target
        '''

        #global list to store our successful combinations

        result = []
        


        #deploy berious recursive function and let recursive magic build out our decision tree

        def dfs(i,substring):

            #make a base case that works, in this case we want to stop when the sum of our substring is == our target if it is already greater, dont add and just end recursive call
            if sum(substring)==target:
                result.append(substring)
                return
            elif sum(substring)>target or i >= len(nums):
                return
            else:
                
                dfs(i,substring+[nums[i]])


                #2.) exclusive 
                dfs(i+1,substring)
        dfs(0,[])
        return result






                    
