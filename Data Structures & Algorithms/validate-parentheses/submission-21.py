class Solution:
    def isValid(self, s: str) -> bool:
       
        stack=[]

        opening=['[','(','{']
        closing=[']',')','}']

        for char in s:
            if char in opening:
                stack.append(char)

            if char in closing:
                if not stack:
                    return False
                compare=stack.pop()

                if char==')' and compare!='(':
                    return False
                if char=='}' and compare!='{':
                    return False
                if char==']' and compare!='[':
                    return False

        return len(stack)==0