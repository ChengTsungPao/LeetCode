class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        memo = {}
        def recur(index, k):
            
            if (index, k) not in memo:
            
                if k == 0:
                    return [[]]
                elif index >= n + 1:
                    return []

                ans = recur(index + 1, k)
                for ret in recur(index + 1, k - 1):
                    ans.append([index] + ret)
                    
                memo[index, k] = ans
                
            return memo[index, k]
                        
        return recur(1, k)