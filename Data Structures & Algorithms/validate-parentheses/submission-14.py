class Solution:
    def isValid(self, s: str) -> bool:
        
        stack=[]

        dic={'}':'{',')':'(',']':'['}


        for x in s:
            if x in list(dic.values()):
                stack.append(x)
            else:
                if x and not stack:
                    return False
                
                if stack:
                    value=stack.pop()
                    if value != dic[x]:
                        return False
        return len(stack)==0