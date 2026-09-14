class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        '''
        for all possible pairings we can either choose or not choose
        from the selected set.

                                    [][1,2,3]
                        [1][2,3].           [][2,3]
                     [1,2][3].  [1][3]      [].     [2][3]


        '''
        


        results=[]


        def recursion(sublist,choices):
            #if choices is [] stop

            if choices == []:
                results.append(sublist)
                return
            
            orig=sublist.copy()
            
            add_choose=sublist.copy()
            add_choose.append(choices[0])
            
            no_add=choices[1:]

            no_add2=no_add.copy()

            print(f'add choose: {add_choose}    no_add: {no_add}')
            print(f'orig: {orig}    no_add2: {no_add2}')

            recursion(add_choose,no_add)
            recursion(orig,no_add2)

        recursion([],nums)
        return results