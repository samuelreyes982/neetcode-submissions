#import alphanum
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r and l<len(s)-1 and r >0:
            
            #alpha num handling
            if s[r].isalnum()==False and r >0:
                r-=1
                continue
                #print("1")
               
                
             
            if s[l].isalnum()==False and l<len(s)-1:
                l+=1
                #print("2")
                continue
                
            if s[l].lower()!=s[r].lower():
                #print("3")
                return False
            l+=1
            r-=1
        return True