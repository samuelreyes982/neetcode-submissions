class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        for x in s:
            if x not in d:
                d[x]=1
            else:
                d[x]=d[x]+1
        
        k={}
        for x in t:
            if x not in k:
                k[x]=1
            else:
                k[x]=k[x]+1

        if d==k:
            print("d",d)
            print("k",k)
            return True
        else:
            return False
        