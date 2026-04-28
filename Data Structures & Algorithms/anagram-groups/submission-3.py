class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}

        for item in strs:
            key=tuple(sorted(item))
            if key in dic:
                dic[key].append(item)
            else:
                dic[key]=[item]
        res=dic.values()
       
        return list(dic.values())