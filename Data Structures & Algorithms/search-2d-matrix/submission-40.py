class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        '''
        strategy for this is a double search for right row, then searching for right
        slot in row, both using binary search
        '''
        #i think i been using middle but we already know middle cant be the answer
        # we need middle+1 because we already know middle cant be it because we already checked
        #find correct row

        #find if row possible
        left=0
        right=len(matrix)-1
        possible_row=False
        row= 'not found'
        while right>=left:

            middle=(left+right)//2

            if matrix[middle][0]<=target and matrix[middle][-1]>=target:
                possible_row=True
                row=middle
                break
            elif matrix[middle][0]<target and matrix[middle][-1]<target:
                left=middle+1
            else:
                right=middle-1
        
        if row=='not found':
            return False

        #if we found a possible row we check that row to see if it contains target
        if possible_row:
            left=0
            right=len(matrix[row])-1
            while right>=left:
                middle=(left+right)//2
                if matrix[row][middle]==target:
                    return True
                elif matrix[row][middle]>target:
                    right=middle-1
                else:
                    left=middle+1

        return False