class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        for item in s:
            if item in [')','}', ']']:
                if stack==[]:
                    return False
                match=stack.pop()
                if item==')' and match!= '(':
                    return False
                if item=='}' and match!= '{':
                    return False
                if item==']' and match!= '[':
                    return False
            else:
                stack.append(item)
        return stack==[]