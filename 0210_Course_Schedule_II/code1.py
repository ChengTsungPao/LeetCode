class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = collections.defaultdict(set)
        for prerequisite in prerequisites:
            graph[prerequisite[0]].add(prerequisite[1])
        
        empty = set()
        for course in range(numCourses):
            if course not in graph:
                empty.add(course)
        
        ans = []
        while empty:
            element = empty.pop()
            ans.append(element)
            for course in list(graph.keys()):
                if element in graph[course]:
                    graph[course].remove(element)
                    
                    if graph[course] == set():
                        del graph[course]
                        empty.add(course)
                        
        if len(graph) == 0:
            return ans
        else:
            return []