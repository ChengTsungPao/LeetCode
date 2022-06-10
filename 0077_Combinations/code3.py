class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        memo = {}
        def recur(index, k):
            
            if (index, k) not in memo:
            
                if k == 0:
                    return [[]]

                ans = []
                for i in range(index, n - k + 2):
                    for ret in recur(i + 1, k - 1):
                        ans.append([i] + ret)
                        
                memo[index, k] = ans
                    
            return memo[index, k]
        
        return recur(1, k)