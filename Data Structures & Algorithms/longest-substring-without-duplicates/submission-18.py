class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen=set()
        left=0
        right=left
        max_seq=0
        #edge case for " "
        if len(s)==1:
            return 1

        while right<len(s):
            #havent seen this letter
            if s[right] not in seen:
                seen.add(s[right])
                right+=1
                max_seq=max(max_seq,right-left)
            
            #have seen this letter
            #restart interval by making new start point
            else:
                left+=1
                right=left
                seen=set()
        return max_seq