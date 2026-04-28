class Solution:
        def subsets(self, nums: List[int]) -> List[List[int]]:
            '''
            return all possible subset combinations of the numeric array nums . no duplicates, and the order does not matter, for us we are going to make a dfs decision tree, which 
            splits at each node with left being the exclusive not including the next number in our combination, while right does include the next node. we are going to do this recursivley until
            the we are at the end of the string
            '''

            #global string that is going to store all of our combinations
            result=[]


            #now we are going to use a recursive helper to create this decision tree.

            #i is the index, substring is the current string we will or wont be adding to
            def dfs(i,substring):
                #remember when doing recursion we should really think out bases cases first
                # if we reach the end of the potential string we have nothing to add, thus we should be just stop, but when we stop we should add whatever substring we were passed in, into the result
                if i ==len(nums):
                    result.append(substring)
                    return 
                #if we still have potential numbers to include or exclude then we should have 2 different recursive calls for both

                # 1.) this will be our inclusive call , aka add to
                dfs(i+1,substring+[nums[i]])
                
                # 2.) this will be our excluding call which will leave out the potential num at index i, but will have the potential to make both of the same decisions after
                dfs(i+1,substring)

            #we are gonna run our helper starting at index 0, and then passing in a empty list so we can get every combination

            dfs(0,[])


            #we are going to return our list after all of our combinations have been added 

            return result


        