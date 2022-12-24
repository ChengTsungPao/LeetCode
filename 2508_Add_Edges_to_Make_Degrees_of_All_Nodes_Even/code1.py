class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        
        cacheEdges = set()
        countEdges = collections.Counter()
        for u, v in edges:
            cacheEdges.add((u, v))
            cacheEdges.add((v, u))
            countEdges[u] += 1
            countEdges[v] += 1
            
        oddDegreeNode = set()
        for k, v in countEdges.items():
            if v % 2 == 1:
                oddDegreeNode.add(k)
        
        num_of_oddDegree = len(oddDegreeNode)
        
        if num_of_oddDegree == 0:
            return True
        
        elif num_of_oddDegree == 2:
            if tuple(oddDegreeNode) not in cacheEdges:
                return True
            
            oddNode1, oddNode2 = oddDegreeNode
            for node in range(1, n + 1):
                if node not in oddDegreeNode and (oddNode1, node) not in cacheEdges and (oddNode2, node) not in cacheEdges:
                    return True
                
        elif num_of_oddDegree == 4:
            oddDegreeNodeList = list(oddDegreeNode)
            for i in range(4):
                for j in range(i + 1, 4):
                    m, n = set(range(4)) - set([i, j])
                    if (oddDegreeNodeList[i], oddDegreeNodeList[j]) not in cacheEdges and (oddDegreeNodeList[m], oddDegreeNodeList[n]) not in cacheEdges:
                        return True
                    
        return False