class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        memo = {}
        def recur(index, n, k):
            
            if (index, n, k) not in memo:
            
                if n == 0 and k == 0:
                    return [[]]
                elif n < 0 or k == 0 or index >= 10:
                    return []

                ans = []
                for i in range(index, 9 + 1):
                    for ret in recur(i + 1, n - i, k - 1):
                        ans.append([i] + ret)
                        
                memo[index, n, k] = ans
                    
            return memo[index, n, k]
        
        return recur(1, n, k)