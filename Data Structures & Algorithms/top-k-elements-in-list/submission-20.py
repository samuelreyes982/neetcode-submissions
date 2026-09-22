class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        we will use bucket sort in order to get an o(n) time
        '''

        #set buckets
        freq=[[ ] for _ in range(len(nums)+1)]

        #count freq with dic
        dic={}

        for x in nums:
            dic[x]=dic.get(x,0)+1
        
        #print(freq)
        #add to bucket
        for key,value in dic.items():
            freq[value].append(key)
        #print(freq)
        #pop off last item
        res=[]
        for i in range(len(freq)-1,-1,-1):
            #print(f'freq[i]. {freq[i]}')
            while len(freq[i])>0:
                res.append(freq[i].pop())
                if len(res)==k:
                    return res