class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        
        dic={}


        for x in strs:
            key=tuple(sorted(x))

            if key in dic:
                dic[key].append(x)
            else:
                dic[key]=[x]



        return list(dic.values())