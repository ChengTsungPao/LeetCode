class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        n = len(strs)
        m = len(strs[0])
        
        def convert(strs):
            status = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    status[i][j] = ord(strs[i][j]) - 97
            return status
        
        def isSorted(a, b, index, status):
            for i in range(a + 1, b + 1):
                if status[i - 1][index] > status[i][index]:
                    return False
            return True
        
        def getContinueRegion(a, b, index, status):
            ret = []
            ch = strs[a][index]
            start = a
            for i in range(a, b + 1):
                if strs[i][index] != ch:
                    ret.append((start, i - 1))
                    ch = strs[i][index]
                    start = i
            ret.append((start, b))
            return ret
        
        status = convert(strs)
        
        ans = 0
        layer = 0
        que = collections.deque([(0, n - 1)])
        while que and layer < m:
            
            newQue = collections.deque()
            oldQue = que.copy()
            
            while que:
                i, j = que.pop()
                
                if not isSorted(i, j, layer, status):
                    ans += 1
                    newQue = oldQue.copy()
                    break
                    
                for start, end in getContinueRegion(i, j, layer, status):
                    if start == end:
                        continue
                    newQue.appendleft((start, end))
                    
            que = newQue.copy()
            layer += 1
            
        return ans