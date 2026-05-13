class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        seen=set()
        results=[]


        def search(sublist,i):

            #print(sublist)
            
            if sum(sublist)>target or i>len(nums)-1:
                return
            
            if sum(sublist)==target:
                key= tuple(sublist)

                if key not in seen:
                    results.append(sublist)
                    seen.add(key)

            
            #stay at index
            copy=sublist.copy()
            copy.append(nums[i])
            search(copy,i)

            #go past
            copy=sublist.copy()
            #copy.append(nums[i])
            search(copy,i+1)


            return

        search([],0)
        return results
