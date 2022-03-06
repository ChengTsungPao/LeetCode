class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        for course, nextCourse in prerequisites:
            graph[course].append(nextCourse)
            
        def dfs(course, curFound, found):
            if course in curFound:
                return True
            
            found.add(course)
            for nextCourse in graph[course]:
                if dfs(nextCourse, curFound | set([course]), found):
                    return True
            
        
        found = set()
        for startCourse in range(numCourses):
            if startCourse in found:
                continue
            
            if dfs(startCourse, set(), found):
                return False
            
        return True