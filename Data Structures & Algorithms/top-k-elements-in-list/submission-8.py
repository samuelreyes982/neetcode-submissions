class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        '''
        for topkfrequent number we are gonna use bucket sort
        bnasically make a dic with all the values

        then place each of them in a "bucket" the frequency of the 
        number will be the index of a list
        '''
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1
        
        #bucket

        bucket=[]
        for _ in range(len(nums)+1):
            bucket.append([])
        print(dic)
        for key in dic.keys():
            print(f'value {dic[key]}')
            bucket[dic[key]].append(key)
        
        res=[]
        print(bucket)
        #print(f'len bucket {len(bucket)} len nums {len(nums)}')
        for i in range(len(bucket)-1,-1,-1):
            #print(i)
            while bucket[i]!=[]:
                x=bucket[i].pop()
                res.append(x)
                if len(res)==k:
                    return res


        