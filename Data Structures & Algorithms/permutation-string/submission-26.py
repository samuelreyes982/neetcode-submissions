class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        dic={}

        for char in s1:
            if char in dic:
                dic[char]+=1
            else:
                dic[char]=1
        

        dic2={}



        left=0
        right=0

        for i in range(len(s2)):
            print(f'dic {dic}')
            print(f'dic2 {dic2}')
            print(f'right : {right}. left: {left}')
            
            
            
            #item in str1
            if s2[i] in s1:
                #item in str1 and in dictionary2
                if s2[i] in dic and s2[i] in dic2 and dic[s2[i]]==dic2[s2[i]] :
                    
                    dic2[s2[left]]-=1
                    left+=1
                    
                print(f'added {s2[i]} to dic2') 
                print('*******************************')
                dic2[s2[i]]= 1+dic2.get(s2[i],0)
                right+=1
            else:
                dic2={}
                left+=1
                right+=1
            #check if dic are equal
            if dic2==dic:
                return True
            if i==len(s2)+1:
                return False

        return False