class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        constraints are low so probably a brute force solution
        
        so basically for each number we can choose it or not choose it, and
        add it to our current substring, by the end well have a substring
        where we choose every string, and well have one were we choose 0 strings

        then we can cross referenece with a seen set so that we know which ones are
        already added, so we dont add twice
        '''
        results=[]
        seen=set()
        def dfs(substring,choices):
            #choices is basically a list of our choices
            #substring is our current list of prev choices


            #make sure weve exhausted all choices

            if len(choices)==0:
                key= tuple(sorted(substring))

                if key not in seen:
                    seen.add(key)
                    results.append(sorted(substring))
                    #terminate call
                return


            #if we still have more choices to make lets keep choosing or not choosing
            #an item
            
            
            #include item
            new_substring=substring[:]
            new_substring.append(choices[0])
            new_choices= choices[1:]
            dfs(new_substring,new_choices)

            #skip item aka remove it from choices but not add it
            skip_substring=substring[:]
            dfs(skip_substring,new_choices)
        
        
        dfs([],nums)
        return results







