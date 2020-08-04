class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) <= 1: return True
        graph = collections.defaultdict(list)
        for pos in prerequisites:
            graph[pos[0]] += [pos[1]]
        course = set(range(numCourses))
        def dfs(node, preivous):
            nonlocal course
            course -= set([node])
            if node in preivous:
                return True
            for pos in graph[node]:
                if dfs(pos, preivous | set([node])):
                    return True
        while course:
            tmp = list(course)[0]
            if dfs(tmp, set()):
                return False
        return True
