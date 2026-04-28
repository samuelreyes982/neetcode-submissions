class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        the intuition behind this problem is that we want to 
        use a clever trick by using a set to hold the number in array
        then we go over each element once and figure out if it
        is part of a sequence or not, then we update our counter for
        sequence

        on average a search on an unsorted array is o(n)
        an average search for an unsorted set is o(1)
        '''
        longest=0
        set_on_array=set(nums)
        for num in nums:
            if num-1 not in set_on_array:
                start=num
                count=0
                while start in set_on_array:
                    start+=1
                    count+=1
                longest=max(longest,count)
        return longest
