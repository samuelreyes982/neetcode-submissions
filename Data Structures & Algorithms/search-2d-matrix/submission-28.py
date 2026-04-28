class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:



        #2d binary search
        '''
        strategy would be to search for correct row first

        then once in correct row do binary search over the columns there 
        and see if our target exists
        '''

        #lets find our row first 

        len_row=len(matrix)
        len_col=len(matrix[0])

        left=0
        right=len_row-1
        #using binary search
        target_row=-1
        while left<=right:
            mid=(left+right)//2

            if target< matrix[mid][0]:
                right=mid-1
            elif target> matrix[mid][len_col-1]:
                left=mid+1
            else:
                #we found our potential row
                target_row=mid
                print('target row found')
                break
        #if target_row =-1 means we no potential rows return false immediatly
        if target_row==-1:
            return False

        #now we need to search our target row, using binary search

        left=0
        right=len_col-1

        while left<=right:
            middle=(left+right)//2
            print(f'left: {left} right: {right}. middle: {middle}')
            print(f'target : {target}.    middle: {matrix[target_row][middle]}')
            if target<matrix[target_row][middle]:
                right=middle-1
            elif target>matrix[target_row][middle]:
                left=middle+1
            else:
                print('found value')
                return True
        #we could not locate value
        return False



        