class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        left=0
        right=0
        maxx=0
        seen=set()

        while right<len(s):

            if s[right] in seen:
                #print(f'right: {right} left: {left} not valid.   s[right]{s[right]}.   seen: {seen}')
                maxx=max(maxx,right-left)
                seen.remove(s[left])
                left+=1
            else:
                #print(f'right: {right} left: {left} valid.   s[right]{s[right]}.   seen: {seen}')
                seen.add(s[right])
                maxx=max(maxx,right-left)
                right+=1
        maxx=max(maxx,right-left)
        return maxx

        