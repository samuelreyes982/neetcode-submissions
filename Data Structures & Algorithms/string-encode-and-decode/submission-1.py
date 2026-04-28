class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded_string=""
        for string in strs:
            encoded_string+= "#"+str(len(string))+"."+string

        
        
        print(f'encoded string : {encoded_string}')
        return encoded_string

        

    def decode(self, s: str) -> List[str]:
        decoded_list=[]
        i=0
        while i < len(s):
            print(f'index.  :{i}      letter:    {s[i]}')
            if s[i]=="#":
                temp=""
                while(s[i+1]!="."):
                    temp+=s[i+1]
                    i+=1
                    

                word_len=int(temp)
                decoded_list.append(s[i+2:i+2+word_len])
            i+=word_len+2

            #  "["#2we","#3say","#1:","#3yes","#10!@#$%^&*()"]"






        
        return decoded_list
    