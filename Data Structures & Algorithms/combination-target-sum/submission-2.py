class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results=[]
        seen=set()

        def dfs(substring):

            #check if sum choices is too large, if it is terminate recursive call
            print(f'substring {substring}')
            if sum(substring)>target:
                return
            if sum(substring)==target:
                key=tuple(sorted(substring))
                if key not in seen:
                    results.append(substring)
                    seen.add(key)
                return
            # substring does not add to target or over so we keep adding
            
            for x in nums:
                new=substring.copy()
                new.append(x)
                dfs(new)
            return
        dfs([])
        return results