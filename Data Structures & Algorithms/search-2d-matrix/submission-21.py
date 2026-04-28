class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #when doing a 2d matrix problem lets start by defining our boundaries

        col_length=len(matrix)
        row_length=len(matrix[0])

        '''
        first we want to figure out which row to search first, we
        can deduce this by looking at the first number in each column, 
        because our target needs to be larger than the first number but less
        then the next number 

        '''
        self.search_col=0
        #binary search for columns first element for correct row
        def find_col():
            left=0
            right=len(matrix)-1
            print(f'left: {left}      right:{right}')
            #print(f'right :    {right}')
            while left<=right:
                middle=(left+right)//2
                print(f'middle :   {middle}   ')
                #print(f' matrix middle {matrix[middle]}')
                if target>matrix[middle][-1]:
                    left=middle+1

                elif target<matrix[middle][0]:
                    right=middle-1
                else:
                    print("found")
                    print(matrix[middle])
                    return matrix[middle]     
            return False


      
      #binary search a single row for target
        def search(array,target):
            
            
            left=0
            right=len(array)-1

            while left<=right:
                middle=(left+right)//2
                
                #if middle bigger than target we need to shift left
                if array[middle]>target:
                    right=middle-1
                #if middle smaller than target we need to shift right
                elif array[middle]<target:
                    left=middle+1
                else:
                    return True
            return False
        array=find_col()
        if array==False:
            return array
        else:
            return search(array,target)        

                
    



        

        