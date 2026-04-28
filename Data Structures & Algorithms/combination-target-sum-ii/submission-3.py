class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        seen=set()
        candidates.sort()
        def dfs(index,substring):
            print(f'substring {substring}')
            #no use in continuing
            if sum(substring)>target:
                return
            #if we equal target we potentially have a match
            
            #todo create key for a set check if path already in result

            key=tuple(sorted(substring))
            if key in seen:
                return
            
            if sum(substring)==target:
                result.append(substring)
                seen.add(key)
                return
            if index>=len(candidates):
                return
            #else our substring too small we need to keep adding elements

            
                #INCLUDE
            temp=substring.copy()
            temp.append(candidates[index])
            dfs(index+1,temp)

                #exclude
            temp2=substring.copy()
            dfs(index+1,temp2)
            return
        dfs(0,[])
        return result