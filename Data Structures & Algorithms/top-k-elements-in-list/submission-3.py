class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        '''
        we initialize all values of dictonary to 0 then 
        we iterate through the list in order to create a key value pair
        showing each item and the amount of times it shows up.
        now we need to sort the dictionary from most frequent to 
        least and make it contain k items

        '''
        for item in nums:
            dictionary[item]=0
        for item in nums:
               
            
            dictionary[item]+=1

        print(dictionary)
        '''
        now we need to sort the dictionary from most frequent to 
        least and make it contain k items
        '''
        
        
        res=[]
        
        sortednum=sorted(dictionary,key=dictionary.get, reverse=True)
        print('sortednum:',sortednum)
        return sortednum[:k]

