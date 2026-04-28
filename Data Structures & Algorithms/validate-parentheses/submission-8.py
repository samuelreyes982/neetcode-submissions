class Solution:
    def isValid(self, s: str) -> bool:
        
        dic={'{':'}','[':']','(':')'}
        stack=collections.deque()
        for item in s:
            print(f'item {item}')
            if item in dic:
                stack.append(item)
            else:
                if not stack or dic[stack.pop()]!=item:
                    return False
        return len(stack)==0