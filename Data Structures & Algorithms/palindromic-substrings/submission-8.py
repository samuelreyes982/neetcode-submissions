class Solution:
    def countSubstrings(self, s: str) -> int:
        

        count=0
        palin=[]

        #odd length palindromes
        for i in range(len(s)):
            left=i
            right=i

            while left>=0 and right<=len(s)-1:
                if s[left]==s[right]:
                    count+=1
                    palin.append(s[left:right+1])
                else:
                    break
                left-=1
                right+=1
        #even length palindromes
        for i in range(len(s)):
            left=i
            right=i+1

            while left>=0 and right<=len(s)-1:
                if s[left]==s[right]:
                    count+=1
                    palin.append(s[left:right+1])
                else:
                    break
                left-=1
                right+=1
        print(palin)
        return count
