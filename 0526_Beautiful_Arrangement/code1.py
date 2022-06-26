class Solution:
    def countArrangement(self, n: int) -> int:
        
        valid = collections.defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i % j == 0 or j % i == 0:
                    valid[i].append(j)
        
        visited = set()
        def recur(i):
            if i >= n + 1:
                return 1
            
            ans = 0
            for j in valid[i]:
                if j in visited:
                    continue
                
                visited.add(j)
                ans += recur(i + 1)
                visited.remove(j)
                
            return ans
        
        return recur(1)