class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        ''' lets do bucket sort


                                      1  2   3
        array -> length of nums: [0] [1] [2] [3] [4] [5] [6]
        '''

        bucket_sort_array=[]
        #create 2d list
        for j in range(len(nums)+1):
            bucket_sort_array.append([])
        dic={}
        for number in nums:
            dic[number]=dic.get(number,0)+1
            #print(f'dic[number]{dic[number]}.  number {number}')
            #print(f'bcuket sort {bucket_sort_array}')
            #bucket_sort_array[dic[number]].append(number)
        for item in dic.keys():
            bucket_sort_array[dic[item]].append(item)
        res=[]
        #print(f'bcuket sort {bucket_sort_array}')
        for i in range(len(bucket_sort_array)-1,-1,-1):
            if len(res)==k:
                return res
            gate=True
            while gate:
                while len(bucket_sort_array[i])==0:
                    if i ==0 and i==[]:
                        return res 
                    i=i-1
                    #print(f'changed i {i}')
                #print(f'res {res}')   
                #print(f'i : {i}')
                item = bucket_sort_array[i].pop()
                if item not in res:
                    gate=False
            res.append(item)
        return res