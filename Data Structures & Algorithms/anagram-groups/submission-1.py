class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for s in strs:
            key=tuple(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key]=[s]
        res=[]

        for x in dic.values():
            res.append(x)
        return res 
        