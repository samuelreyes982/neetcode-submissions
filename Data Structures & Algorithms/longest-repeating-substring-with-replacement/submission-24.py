class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxx=0
        dic={}

        left=0
        right=0
        for i in range(97,123,1):
            char=chr(i)
            dic[char.upper()]=0
        #make dic for alphabet
        #print(dic)

        while right<len(s):
            dic[s[right]]+=1

            #valid
            replacements=(right-left+1)-max(dic.values())   

            if replacements<=k:
                maxx=max(maxx,right-left+1)
                right+=1
            #not valid
            else:
                dic[s[left]]-=1
                left+=1
                right+=1

        return maxx

            
        