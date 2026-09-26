class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        so we are gonna do a sliding window, with a dictionary keeping track of
        the letters we have in our string, that is also the same length as our
        s1
        '''

        if len(s1)>len(s2):
            print(len(s1))
            print(len(s2))
            return False
        dic={}
        dic2={}

        for x in range(97,(97+26),1):
            dic[chr(x)]=0
            dic2[chr(x)]=0
        #print(dic)
        #print(dic==dic2)
        for x in range(len(s1)):
            dic[s1[x]]+=1
            dic2[s2[x]]+=1
        
        #print(dic)
        #print(dic2)
        
        left=0
        right=len(s1)-1

        
        while right<len(s2)-1:
            
            print(f'left {left}')
            print(f'right {right}')
            print(dic2)
            print('*************************************************************')
            
            if dic==dic2:
                
                return True
            dic2[s2[left]]-=1
            left+=1
            right+=1
            dic2[s2[right]]+=1
        return dic==dic2
       