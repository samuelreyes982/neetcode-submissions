class Solution:
    def countSubstrings(self, s: str) -> int:
        num_palindrome=0

        for i in range(len(s)):
            l=i
            r=i
            #boundary check
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if s[l]==s[r]:
                    num_palindrome+=1
                l-=1
                r+=1
        print(f'after loop 1 : {num_palindrome}')

        #this is to find len(2)
        for i in range(len(s)):
            l=i
            r=i+1
            #boundary check
            while l>=0 and r<=len(s)-1 and s[l]==s[r]:
                if s[l]==s[r]:
                    num_palindrome+=1
                l-=1
                r+=1



        #this is for even index
        return num_palindrome
        # i=0:a,i=1:a, i=1:aaa,i=2:a,


