class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        mapping={}

        res=0
        left=0
        #char will be our right pointer
        for right in range(len(s)):
            #retrieve mapping from dictionary and increment it, return 0 if it doesnt exist 
            #bringing the total to 1
            mapping[s[right]]= 1 + mapping.get(s[right],0)
            print(f'left   : {left}    right: {right}       mapping:  {mapping}')
            #check if it is a valid sequence

            if (right-left+1) - max(mapping.values()) <= k:
                
                res = max(res,right-left+1) 
            
            else:
                
                
                mapping[s[left]]= mapping.get(s[left]) - 1

                print(f's[left]    :{s[left]}       left: {left}')
                #print(s)
                left=left+1
            
        return res

            


        