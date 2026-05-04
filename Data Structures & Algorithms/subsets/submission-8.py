class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[]
        seen=set()
        def dfs(choices,string):
            #empty string holding our results
            
            
            '''
            when do we end recursion ?

            1.) no more choices left

            
            '''
            if choices==[]:
                key=tuple(string)
                if key not in seen:
                    seen.add(key)
                    results.append(string)
                    return
            

            #otherwise we keep figuring out more choices
            #print(f'choices : {choices}')
           
                #with choice in string
            temp1=string.copy()
            temp1.append(choices[0])


                #without choice in string
            temp2=string.copy()

            new_choices=choices.copy()    
            new_choices.remove(choices[0])

            dfs(new_choices,temp1)     
            dfs(new_choices,temp2)     
       
                
        dfs(nums,[])
        return results

