class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        nextCourses = collections.defaultdict(set)
        preCourses = collections.defaultdict(set)
        for course, nextCourse in prerequisites:
            nextCourses[course].add(nextCourse)
            preCourses[nextCourse].add(course)
            
        que = collections.deque()
        for course in range(numCourses): 
            if len(preCourses[course]) == 0:
                que.appendleft(course)
                del preCourses[course]
            
        while que:
            course = que.pop()
            
            for nextCourse in nextCourses[course]:
                preCourses[nextCourse] -= set([course])
                if len(preCourses[nextCourse]) == 0:
                    que.appendleft(nextCourse)
                    del preCourses[nextCourse]           
            
        return len(preCourses) == 0  