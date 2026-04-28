class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #for this we are going to do a sliding window technique


        seen=set()

        left=0
        right=0

        maxx=0

        
        print(f'len(s): {len(s)}')
        if len(s)<=1:
            return len(s)
        while right<len(s):
            #growing sliding window
            if s[right] not in seen:
                seen.add(s[right])
                right= right+1

            elif s[right] in seen:
                #resetting sliding window
                maxx=max(maxx,right-left)
                left=left+1
                right=left
                seen=set()
        maxx=max(maxx,right-left)
        return maxx


'''
l=0
r=1

maxx=0
seen={'x'}
'''

        