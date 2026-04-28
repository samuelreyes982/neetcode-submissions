class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        for example nums=[1,2,3]
        
        [placeholder],[placeholder],[placeholder]

        [3 choices]*[2 choices]*[1 choice]-> possible number of permutations

        we want to make some kind of decision tree with all possible permutations, and then return that path, although
        we dont want duplicate sets so order matters

        '''
        result=[]
        seen=set()


        #recursively

        def dfs(i,subset):
            
            key=tuple(subset)
            print(f'length of subset :{len(subset)}')
            if len(subset)==len(nums) :
                print(f'key:      {key}')
                if key not in seen:
                    seen.add(key)
                    result.append(subset[:])
                return
            if i >=len(nums):
                return
            if nums[i] in subset:
                return dfs(i+1,subset)    
            
            
            subset.append(nums[i])
            print(f'inclusive subset {subset}')
            dfs(0,subset)

            subset.pop()

            dfs(i+1,subset)

        for j in range(len(nums)):
            
            dfs(j,[])
        return result


        

