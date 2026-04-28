class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        so the intuition behind this question is that we want to detect cycles
        in our courses and if there is a cycle we return false.
        if we traverse all of the courses until we return an empty list
        we then know the course is completable, and when we verify that
        all courses are completeable, we can then return True

        '''

        #first lets initialize our dictionary with empty lists as the val 
        seen=set()
        dic={}
        for i in range(numCourses):
            dic[i]=[]
        
        for course,prereq in prerequisites:
            dic[course].append(prereq)
        
        print(dic)
        
        #now we create a dfs to traverse every preq for a course
        # when we get to a leaf node, aka empty we know we can stop searching
        def dfs(course):
            #leaf
            if course==[]:
                return True
            #cycle detected return false
            print(f'seen   :    {seen}   course:   {course}')
            print(f'course in seen : {course in seen}')
            if course in seen:
                print('[CYCLE DETECTED]')
                return False
            # we still have to finish traversing our path
            seen.add(course)
            # lets keep checking prereqs
            for prereq in dic[course]:
                print(f'course:     {course}   prereq:     {prereq}')
                if dfs(prereq)==False:
                    return False
            seen.remove(course)
            # marking empty basically marks it complete to avoid extra work
            dic[course]=[]
            return True
        res=[]
        for course in range(numCourses):
            print(f'dfs(course):     {dfs(course)}')
            res.append(dfs(course))

        
        if False in res:
            return False
        return True