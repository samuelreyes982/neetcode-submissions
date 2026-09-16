class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        '''
        for combinations we are gonna need a set for tracking results
        probably some kind of sorted set


        we can do a tree right, where we use every choice, then do it 
        again and select every choice 

        2-2
        2-5
        2-6
        2-9
        
        5-2
        5-5
        5-6
        5-9

        6-2
        6-5
        6-6
        6-9

        for every choice in the set, we add every number in nums to it

        we will have alot of branches, we should kill recursion when our sum
        reaches target, 
        .....

        
        


        '''
        seen=set()
        result=[]
        nums=sorted(nums)

        def search(sublist):
            #when our sublist sum is too big terminate
            #pruning
            key=tuple(sorted(sublist))
            if key in seen:
                return

            
            
            seen.add(key)
                

            if sum(sublist)==target:
                
                result.append(sublist)
                return
            if sum(sublist)>target:
                return

            for item in nums:
                newSublist=sublist.copy()
                newSublist.append(item)
                search(newSublist)
            return

        search([])
        return result


