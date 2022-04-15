class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = collections.defaultdict(list)
        parent = collections.defaultdict(int)
        for nextCourse, course in prerequisites:
            graph[course].append(nextCourse)
            parent[nextCourse] += 1
            
        total_edge = len(prerequisites)
        que = collections.deque()
        for course in range(numCourses):
            if parent[course] == 0:
                que.appendleft(course)
                
        while que:
            course = que.pop()
            
            for nextCourse in graph[course]:                
                total_edge -= 1
                parent[nextCourse] -= 1
                if parent[nextCourse] == 0:
                    que.appendleft(nextCourse)
                    
        return total_edge == 0