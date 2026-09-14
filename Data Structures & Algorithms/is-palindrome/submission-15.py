class Solution:
    def isPalindrome(self, s: str) -> bool:

        '''
        given a sentence, we are gonna compare
        first and last together over and over until 
        no more letter/number to check

        if a letter/number is a sign we skip that one and move one spot
        
        
        
        time complexity:
        (LINEAR)

        space complexity:
        (constant)
        '''


        leftmost=0
        rightmost=len(s)-1



        while leftmost<=rightmost:
            if s[leftmost].isalnum()== False:
                leftmost+=1
            elif s[rightmost].isalnum()==False:
                rightmost-=1
            elif s[rightmost].lower()!=s[leftmost].lower():
                return False
            else:
                rightmost-=1
                leftmost+=1
        return True
        
        