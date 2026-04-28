class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        strategy, use optimized reverse bucket sort
        

        example [ 6, 6 ,6, 5, 10, 4, 4 ]  - note that we have 7 elements so we should have 7 buckets 
        frequency index:[0,1,2,3,4,5,6,7] - number of times spotted
        value:          [[],[5,10],[4],[6],[],[],[],[]]  - 5 and 10 spotted once, 4 spotted twice, 6 spotted 3 times 

        so now we can pop from the end until we have k numbers and re return them into a list and return  
        '''
        #make a dictionary
        count={}

        freq = [[] for i in range(len(nums) + 1)]

        #make an list of empty lists that is len(nums)
        
        #lets populate count

        for num in nums:
            count[num]=1+ count.get(num,0)

        for num,count in count.items():
            freq[count].append(num)

        res=[]

        for i in range(len(freq)-1,0,-1):
            for i in freq[i]:
                res.append(i)
                if len(res)==k:
                    return res



                    
        
        