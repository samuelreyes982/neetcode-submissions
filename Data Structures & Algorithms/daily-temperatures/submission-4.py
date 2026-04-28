class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        at first glance we are trying to compute a value that

        is dependent on a future index of an array

        i think a stack could be a potential solution

        '''
        result=[0]*len(temperatures)


        stack=[]

        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                last=stack.pop()
                days=i-last[1]
                result[last[1]]=days
            stack.append([temperatures[i],i])
        return result

            