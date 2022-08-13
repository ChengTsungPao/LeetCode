class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        n = len(cookies)
        
        container = [0] * k
        
        memo = {}
        def recur(index, container):
            
            key = str(sorted(container)) + "_" + str(index)
            
            if key not in memo:
            
                if index >= n:
                    return max(container)

                ans = float("inf")
                cookie = cookies[index]

                for i in range(k):
                    container[i] += cookie
                    ans = min(ans, recur(index + 1, container))
                    container[i] -= cookie
                    
                memo[key] = ans
                
            return memo[key]
        
        return recur(0, container)