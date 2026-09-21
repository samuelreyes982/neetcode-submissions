class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''


        ok so we may have duplicate numbers, but we cant use duplicate indexes, so we will 
        sort, and then by index we wont allow the same number to be used twice in order
        to cut down the work, but we will use a choose exclude recursion to get our stuff done
        '''

        results=[]
        candidates=sorted(candidates)
        def search(index,sublist,summ):
            if summ==target:
                #print(f'sublist {sublist} summ {summ}')
                results.append(sublist)
                return
            #early prempts
            #print(index)
            if summ>target or index>len(candidates)-1:
                return
            #we hit target
            
            #print(index)
            #we still need to keep going to possibly get a good combination
            #print(index)
            #include
            copy=sublist.copy()

            copy.append(candidates[index])
            search(index+1,copy,summ+candidates[index])


            #exclude
            copy2=sublist.copy()
            #print(index)
            #print(f'sublist{candidates[index]} ,   sublsit[index]+1 {candidates[index+1]}')
            while index+1<=len(candidates)-1 and candidates[index]==candidates[index+1]:
                index+=1
                #print(f'index {index}')
            #print(index)
            search(index+1,copy2,summ)
        search(0,[],0)
        return results






