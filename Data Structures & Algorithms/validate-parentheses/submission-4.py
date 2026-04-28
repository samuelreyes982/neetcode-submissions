class Solution:
    def isValid(self, s: str) -> bool:
        #stack data structure
        stack=[]
        # make mapping for open and closing brackets

        mapping={")":"(", "}":"{", "]":"["}

        for bracket in s:
            '''
            [case]: where there is a close bracket comes first but
            no leading open bracket

            ''' 

            if bracket in mapping.keys() and len(stack)==0:
                return False
            '''
            case where close bracket doesnt match opening bracket in stack
            '''
            if bracket in mapping.keys() and stack[-1] != mapping[bracket]:
                return False
            

            '''
            case where close bracket  matches opening bracket in stack and we pop
            '''
            if bracket in mapping.keys() and stack[-1] == mapping[bracket]:
                stack.pop(-1)

            '''
            case where it is an open bracket
            '''
            if bracket in mapping.values():
                stack.append(bracket)
        if len(stack)>0:
            return False
        else:
            return True





        

            