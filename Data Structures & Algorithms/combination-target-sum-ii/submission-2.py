class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        this is a similar problem to combination sum 1, where we are trying to find the number of combinations that add up to a target, the only difference is that 
        we cant reuse the same element more then once, but i think we will be fine if we approach the only lets sort that as we move up and the sum is too large we return and 
        terminmat5e the funtion call
        

        
        '''

        #global list we are going to append our combinatiuons to
        combinations=[]
        seen= set()


        #dfs recursive function

        def dfs(i,substring):
            #lets establish our base case
            '''
            where we have a bad combination and we want to terminate our recursive loop
            lets define what a bad combination is
            
            1.) we overshot target
            2.) we are out of bounds
            '''
            

            if sum(substring)==target:
                key=tuple(sorted(substring))

                if key not in seen:
                    combinations.append(substring)
                    seen.add(key)
                return



            if sum(substring)>target or i >= len(candidates):
                return


            
            


            #now we want to build out our decision tree, based on if we want to include or exclude some current i, 

            #inclusive
            dfs(i+1,substring+[candidates[i]])


            #exclusive
            dfs(i+1,substring)
        dfs(0,[])
        return combinations
            









                    
