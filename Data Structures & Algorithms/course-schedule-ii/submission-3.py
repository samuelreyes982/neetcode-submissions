class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #build adjacency list
        result=[]
        dic={}
        seen=set()
        for i in range(len(prerequisites)):
            if prerequisites[i][0] in dic:
                dic[prerequisites[i][0]].append(prerequisites[i][1])
            else:
                dic[prerequisites[i][0]]=[prerequisites[i][1]]

        #print(dic)

        #now that we have an adjacencey list
        #we need to check for cycles

        def dfs(course):
            if course in seen:
                return False
            seen.add(course)
            #check adj list
            if course in dic:
                for n in dic[course]:
                    if dfs(n)==False:
                        return False
            seen.remove(course)
            if course not in result:
                result.append(course)
            return True
        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return result
            