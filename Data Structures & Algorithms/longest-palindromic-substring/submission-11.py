class Solution:
    def longestPalindrome(self, s: str) -> str:

        result=s[0:1]
        largest=1

        #even length palindrome
        if True:
            for i in range(len(s)):
                left=i
                right=i
                while right<=len(s)-1 and left>=0:
                    print(s[left:right+1])
                    if s[left]!=s[right]:
                        break

                    if s[left]==s[right]:
                        length=right-left+1
                        if length>largest:
                            result=s[left:right+1]
                            largest=len(result)
                    right+=1
                    left-=1
        #odd length palindrome
        if True:
            for i in range(len(s)):
                left=i
                right=i+1
                while right<=len(s)-1 and left>=0:
                    print(s[left:right+1])
                    if s[left]!=s[right]:
                        break
                    if s[left]==s[right]:
                        length=right-left+1
                        if length>largest:
                            result=s[left:right+1]
                            largest=len(result)
                    right+=1
                    left-=1


        
        
        print(largest)
        return result

        