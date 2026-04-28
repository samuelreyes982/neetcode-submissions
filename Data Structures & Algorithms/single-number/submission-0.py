class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            #print(f'num: {num}')
            temp=res
            res = num ^ res
            print(f'num: {num}    old res:{temp}      new res:   {res}')
        return res