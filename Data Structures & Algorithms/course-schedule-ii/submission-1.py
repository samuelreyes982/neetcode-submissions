class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #first we want to create a dictionary to represent our adjacency list
        seen=set()
        completed=set()
        adj={}
        for i in range(numCourses):
            adj[i]=[]
        result=[]
        #now we want to fill up our adj list with values

        for course,pre in prerequisites:
            adj[course].append(pre)
        def dfs(course):
            
            if course in seen:
                return False
            if course in completed:
                return True    
            if course==[]:
                return True

            seen.add(course)

            for pre in adj[course]:
                if dfs(pre)==False:
                    return False
            seen.remove(course)
            result.append(course)
            completed.add(course)

        for i in range(numCourses):
            if dfs(i)==False:
                return []
        return result