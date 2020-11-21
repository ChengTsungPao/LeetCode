class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        dgraph = collections.defaultdict(list)
        graph = collections.defaultdict(list)
        for pos in connections:
            dgraph[pos[0]] += [pos[1]]
            graph[pos[0]] += [pos[1]]
            graph[pos[1]] += [pos[0]]

        count = 0
        def dfs(node, prenode):
            nonlocal count
            if len(graph[node]) == 1 and node != 0:
                return None
            tmp = set(dgraph[node])
            for pos in graph[node]:
                if pos not in prenode:
                    if pos in tmp:
                        count += 1
                    dfs(pos, prenode | set([pos]))
                    
        dfs(0, set([0]))
        return count