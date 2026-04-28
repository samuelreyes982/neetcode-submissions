class Solution:
    def longestPalindrome(self, s: str) -> str:

        #edge case

        
        
        
        
        largest_palindrome=s[0]

        for i in range(len(s)):
            left=i
            right=i+1
            while right<len(s):
                if s[left]==s[right]:

                    if is_palindrome(s[i:right+1]):
                        x=len(s[i:right+1])
                        if x > len(largest_palindrome):
                            largest_palindrome=s[i:right+1]
                right+=1
        return largest_palindrome



    def is_palindrome(s):

        l=0
        r=len(s)-1

        while l<r:
            if s[l]<s[r]:
                return False
            l+=1
            r-=1
        return True    
