class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        

    def add(self, val: int) -> int:
        #print(f'nums {self.nums}')
        #print(f'val {val}')
        self.nums.append(val)
        #print(f'new nums {self.nums}')
        self.nums=sorted(self.nums)
        return self.nums[-self.k]
        
'''
[1,2,3,3], k=3

[1,2,3,3,3] ->3
[1,2,3,3,3,5] ->3
[1,2,3,3,3,5,6] ->3
[1,2,3,3,3,5,6,7] ->5
[1,2,3,3,3,5,6,7,8] ->6

'''