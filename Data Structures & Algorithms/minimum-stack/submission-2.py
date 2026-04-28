class MinStack:

    def __init__(self):
        stack=[]
        self.stack=stack
        
        
        self.minstack=[]
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack)==0:
            self.minstack.append(val)
        else:
            self.minstack.append(min(val,self.minstack[-1]))
        
        
        

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minstack.pop(-1)

    def top(self) -> int:
        print(self.stack)
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]

        
'''
1
2
0
'''