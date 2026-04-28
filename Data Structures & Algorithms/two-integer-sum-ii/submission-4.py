class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right = len(numbers)-1
        i=0
        while left<right:
            if numbers[left]+ numbers[right]>target:
                right-=1
            if numbers[left]+ numbers[right]<target:
                left+=1
            if numbers[left]+numbers[right]==target:
                print(f'left {left}')
                print(f'right {right}')
           
                
                return [left+1,right+1]

        
        