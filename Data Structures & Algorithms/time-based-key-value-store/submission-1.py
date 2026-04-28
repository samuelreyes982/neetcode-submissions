class TimeMap:

    def __init__(self):

        self.dic={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic.keys():
            self.dic[key].append([value,timestamp])
        else:
            self.dic[key]=[[value,timestamp]]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.dic.keys():
            return ""
        left=0
        right=len(self.dic[key])-1
        temp=""

        while left<=right:
            middle=(left+right)//2
            #if weve found middle
            if self.dic[key][middle][1]==timestamp:
                return self.dic[key][middle][0]
            
            elif self.dic[key][middle][1]<timestamp:
                temp= self.dic[key][middle][0]
                left=middle+1
            elif self.dic[key][middle][1] >timestamp:
                right = middle-1       
        return temp




        
