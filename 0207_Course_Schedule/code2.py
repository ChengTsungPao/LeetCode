class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(set)
        for prerequisite in prerequisites:
            graph[prerequisite[0]].add(prerequisite[1])
        
        empty = set()
        for course in range(numCourses):
            if course not in graph:
                empty.add(course)
                
        while empty:
            element = empty.pop()
            for course in list(graph.keys()):
                if element in graph[course]:
                    graph[course].remove(element)
                    
                    if graph[course] == set():
                        del graph[course]
                        empty.add(course)
         
        return len(graph) == 0