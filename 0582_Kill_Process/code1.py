class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        
        graph = collections.defaultdict(list)
        for node, nextNode in zip(ppid, pid):
            graph[node].append(nextNode)
            
        def recur(node):
            if not node:
                return []
            
            ret = [node]
            for nextNode in graph[node]:
                ret += recur(nextNode)
                
            return ret
            
        return recur(kill)