class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        we are gonna check from the borders of pacific and atlantic and then 
        add all of the ones who can reach atlantic to a set, and all the ones 
        that can reach the pacific to a set. then we are gonna check which 
        ones are in both and append those to a result and then we return that result
        '''
        #lets define boundaries and initiate data structures

        len_row=len(heights)
        len_col=len(heights[0])

        pacific=set()

        atlantic=set()

        result=[]

        #lets mark our nodes reached by pacific first:
        
        def dfs(row,col,set_,prev_val):
            if row>len_row-1 or row<0 or col>len_col-1 or col<0:
                return
            key=tuple([row,col])
            if prev_val>heights[row][col] or key in set_ :
                return 
            set_.add(key)
            dfs(row+1,col,set_,heights[row][col])
            dfs(row-1,col,set_,heights[row][col])
            dfs(row,col+1,set_,heights[row][col])
            dfs(row,col-1,set_,heights[row][col])
        
        
        #adding all row 0 elements to pacific set, then checking if nieghbors are on ascending path towards
        #our node 
        for column in range(len_col):
            #pacific.add(tuple([[0][column]]))
            #we want to call a dfs that recursivley checks paths
            
            dfs(0,column,pacific,heights[0][column])
        #we want to do vertical for pacific
        for row in range(len_row):
            dfs(row,0,pacific,heights[row][0])



        #atlantic
        for column in range(len_col):
            #pacific.add(tuple([[0][column]]))
            #we want to call a dfs that recursivley checks paths
            
            dfs(len_row-1,column,atlantic,heights[len_row-1][column])
        #we want to do vertical for pacific
        for row in range(len_row):
            dfs(row,len_col-1,atlantic,heights[row][len_col-1])





        #lets create our ascending path finder to a set that recursivley searches adjacent nodes
        


        #now that weve concluded which points are in pacific and atlantic we must add those who intersect
        #both to our results

        for row in range(len_row):
            for col in range(len_col):
                key=tuple([row,col])

                if key in pacific and key in atlantic:
                    result.append([row,col])
        return result










        