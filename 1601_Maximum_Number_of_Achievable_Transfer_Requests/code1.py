class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        m = len(requests)
        
        ans = 0
        def backtracking(idx, r, degree):
            nonlocal ans
            
            if idx >= m:
                if all([d == 0 for d in degree]): 
                    ans = max(ans, r)
                return
            
            # non-choose
            backtracking(idx + 1, r, degree)
            
            # choose
            u, v = requests[idx]    
            degree[u] += 1
            degree[v] -= 1
            backtracking(idx + 1, r + 1, degree)
            degree[u] -= 1
            degree[v] += 1
            
        backtracking(0, 0, [0] * n)
        return ans