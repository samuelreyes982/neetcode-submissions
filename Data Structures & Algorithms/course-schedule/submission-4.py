class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        dic={}
        for i in range(len(prerequisites)):
            print(prerequisites[i][0])
            if prerequisites[i][0] in dic:
                dic[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                dic[prerequisites[i][0]]=[prerequisites[i][1]]

        print(f'dic: {dic}')
        
        
        seen=set()
        def dfs(course):
            print(f'dfs(course) :{course}')
            
            if course in seen:
                print('found_loop')
                return False
            seen.add(course)
            if course in dic:
                for x in dic[course]:
                    if dfs(x)==False:
                        return False


            seen.remove(course)
            return True
        for x in dic:
            print(x)
            if dfs(x)==False:
                return False
        return True