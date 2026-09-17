class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left=0
        right=len(numbers)-1

        
        while left<right:

            summ=numbers[right]+numbers[left]

            if summ < target:
                left=left+1
            elif summ>target:
                right=right-1
            else:
                return [left+1,right+1]




        