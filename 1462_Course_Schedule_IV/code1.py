class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        allPrerequisites = [set() for _ in range(numCourses)]
        
        parent = collections.defaultdict(int)
        graph = collections.defaultdict(set)
        for course, nextCourse in prerequisites:
            graph[course].add(nextCourse)
            parent[nextCourse] += 1
            
        que = collections.deque()
        for course in range(numCourses):
            if parent[course] == 0:
                que.appendleft(course)
                
        while que:
            course = que.pop()
            
            for nextCourse in graph[course]:
                allPrerequisites[nextCourse] |= allPrerequisites[course] | set([course])
                
                parent[nextCourse] -= 1
                if parent[nextCourse] == 0:
                    que.appendleft(nextCourse)
        
        ans = []
        for course1, course2 in queries:
            ans.append(course1 in allPrerequisites[course2])
            
        return ans