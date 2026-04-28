class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result=[]
        seen=set()


        def dfs(substring,choices):
            
            
            print(f'substring {substring}.    choices:{choices}')
            
            #base case : length>len(nums)
            #we want only 3 numbers in each set
            key=tuple(substring)
            if len(substring)==len(nums) and key not in seen:
                result.append(substring)
                seen.add(key)
                
            
            #loop
            for i in range(len(choices)):
                temp=substring.copy()
                temp.append(choices[i])
                new_choices=choices.copy()
                new_choices.remove(choices[i])
                dfs(temp,new_choices)

                
            return
        c=nums.copy()
        dfs([],c)
        return result

        