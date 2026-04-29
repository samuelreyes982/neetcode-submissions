class Solution:
    def isPalindrome(self, s: str) -> bool:


        left_pointer=0
        right_pointer=len(s)-1
        while left_pointer<right_pointer:
            
            if s[right_pointer].isalnum() ==False:
                right_pointer-=1
            
            elif s[left_pointer].isalnum()==False:
                left_pointer+=1
            
            elif s[right_pointer].lower() != s[left_pointer].lower():
                print(f'right {s[right_pointer].lower()}  left {s[left_pointer].lower()}')
                return False
            

            else:
                right_pointer-=1
                left_pointer+=1
        return True