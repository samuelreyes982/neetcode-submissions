class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        binary search, is when we are searching through an array and halve the search space
        every time to cut down the time complexity to O(log(n))

        we have 2 items to complete

        1.) find the correct row first using binary search

        2,) find the correct column second using binary search

        using it twice gives O(log m*n)

        '''

        #find correct row

        left=0
        right=len(matrix)-1
        
        #to know if our target is in a row, it must be inbetween or equal the first and last number of that row
        found_row=False
        row=0
        while left<=right:
            mid=(left+right)//2
            print(f'mid {mid}')
            print(f'left {matrix[mid][0]}.   right: {matrix[mid][len(matrix[0])-1]}')
            #print(f'len {len(matrix[0])-1}')
            #print(mid)
            if matrix[mid][0]<=target and matrix[mid][len(matrix[0])-1]>=target:
                #found potential row
                found_row=True
                row=mid
                break
            #too small
            elif matrix[mid][0]<target and matrix[mid][len(matrix[0])-1]<target:
                left=mid+1
            #too big
            else:
                right=mid-1
        #print(row)
        
        #step 2, find column
        print(f'row found {found_row}. row: {row}')
        if found_row==False:
            return False
        

        left=0
        right=len(matrix[0])-1
        found_column=False
        col=0
        while left<=right:
            mid=(left+right)//2

            if matrix[row][mid]>target:
                right=mid-1
            elif matrix[row][mid]<target:
                left=mid+1
            else:
                found_column=True
                column=mid
                break
        if found_column==True:
            return True
        else:
            return False
                


        