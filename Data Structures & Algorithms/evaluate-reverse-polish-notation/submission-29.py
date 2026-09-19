class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        '''
        for ordered sequence like this i feel like we should use a stack

        store the numbers in the stack until we see an operator, 
        then we use the numbers stored in the stack with that operation


        '''

        #result
        stack=[]

        #start from second number

        #stack.append(int(tokens[0]))

        for item in range(len(tokens)):
            
            if tokens[item] not in ['+','-','/','*']:
                stack.append(int(tokens[item]))
                #print(stack)
            else:
                second=stack.pop()
                first=stack.pop()
                computed=0
                
                #print(f'first {type(first)}. second{second}')
                if tokens[item]=='+':
                    computed=first+second
                if tokens[item]=='-':
                    computed=first-second
                if tokens[item]=='*':
                    computed=first*second
                if tokens[item]=='/':
                    computed=int(first/second)
                stack.append(computed)
                #print(stack)
        return stack[0]
        