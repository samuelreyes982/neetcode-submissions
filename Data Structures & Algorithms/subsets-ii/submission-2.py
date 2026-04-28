class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        results=[]

        seen=set()

        def dfs(substring,choices):
            key=tuple(sorted(substring))

            if choices==[] and key not in seen:
                results.append(substring)
                seen.add(key)
                return
            #else we still have choices and we can still add or not add those choices

            for c in choices:
                temp=substring.copy()
                temp.append(c)
                next_set=choices.copy()
                next_set.remove(c)
                #inclusive call
                dfs(temp,next_set)
                #excluding call
                temp2=substring.copy()
                dfs(temp2,next_set)
            return
        s=nums.copy()
        dfs([],s)
        return results

        