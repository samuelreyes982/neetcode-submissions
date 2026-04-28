class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        print('started')
        for item in tokens:
            
            try:
                int(item)
                stack.append(item)
                continue
            except ValueError:

            
            

                #print(f'item is number {item} {item.isnumeric()}')
                while stack:
                    
                    item2=stack.pop()
                    item1=stack.pop()
                    #print(f'stack 1 : {item1} item: {item}.   item2: {item2}')
                    if item=='+':
                        res=int(item1)+int(item2)
                        stack.append(res)
                        break
                    if item=='-':
                        res=int(item1)-int(item2)
                        stack.append(res)
                        break
                    if item=='*':
                        res=int(item1)*int(item2)
                        stack.append(res)
                        break
                    if item=='/':
                        res=int(item1)/int(item2)
                        stack.append(res)
                        break
        print(stack)        
        return int(stack.pop())
        