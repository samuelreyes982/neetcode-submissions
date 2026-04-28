class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        dic2={}

        for letter in s:
            dic[letter]= dic.get(letter,0)+1
        for letter in t:
            dic2[letter]= dic2.get(letter,0)+1

        print(dic)
        return dic==dic2
