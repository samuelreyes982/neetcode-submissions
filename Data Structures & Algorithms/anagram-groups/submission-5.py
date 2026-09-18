class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        ok so we will group together words with the same letters

        1.) we create a key that is a sorted version of the word

        2.) we create a dictionary where we store all matching keys into a list

        3.) return dictionary keys

        '''
        dic={}

        for s in strs:
            key=tuple(sorted(s))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key]=[s]
        return list(dic.values())

        