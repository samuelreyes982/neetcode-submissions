class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        we need to use a stack in order to keep track of items from before and pop them
        when they have an assigned value
        '''


        #init 0 for all so in case of leftovers we can leave them unchanged
        stack=[]
        result=[0]*len(temperatures)
        for i in range(len(temperatures)):
            
            if stack:
                #print(stack)
                #print(stack[-1])
                #print(stack[-1][0])
                #print(i)
                while stack and (stack[-1][0])<temperatures[i]:
                    temp,index=stack.pop()
                    result[index]=i-index
            stack.append([temperatures[i],i])
        return result
                    

