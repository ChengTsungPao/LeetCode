class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        nextCourses = collections.defaultdict(set)
        preCourses = collections.defaultdict(set)
        for nextCourse, course in prerequisites:
            nextCourses[course].add(nextCourse)
            preCourses[nextCourse].add(course)
            
        que = collections.deque()
        for course in range(numCourses): 
            if len(preCourses[course]) == 0:
                que.appendleft(course)
                del preCourses[course]
        
        ans = []
        while que:
            course = que.pop()

            ans.append(course)
            
            for nextCourse in nextCourses[course]:
                preCourses[nextCourse] -= set([course])
                if len(preCourses[nextCourse]) == 0:
                    que.appendleft(nextCourse)
                    del preCourses[nextCourse]           
            
        return ans if len(ans) == numCourses else []