class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left=0
        right=len(numbers)-1

        '''
        the intuition is that there is exactly 1 solution

        and so there are only 2 numbers that will =satisfy targety

        and they are in ascending order

        that means if we use 2 pointers

        one pointing at the beggining of array

        one pointing at the end 

        if both pointers combined are too small, shift left pointer right

        if both pointers combined are too big, shift right pointer left
        '''
        left=0
        right=len(numbers)-1

        while left<=right:
            summ=numbers[left]+numbers[right]
            if summ>target:
                right=right-1
            elif summ<target:
                left=left+1
            else:
                return [left+1,right+1]
        