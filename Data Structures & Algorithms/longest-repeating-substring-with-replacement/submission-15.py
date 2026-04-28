class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        right=0
        dic={}
        maxx=0
        seen=set()
        while right<len(s):
            if right not in seen:
                if s[right] in dic:
                    dic[s[right]]+=1
                else:
                    dic[s[right]]=1
                seen.add(right)
            #check if we have a valid window
            if right-left+1<=max(dic.values())+k:
                maxx=max(maxx,right-left+1)
                right+=1
            else:
                #we move our left pointer forward
                #which means we need to remove that pointer
                #from our dictionary
                dic[s[left]]-=1
                left+=1
        return maxx


        