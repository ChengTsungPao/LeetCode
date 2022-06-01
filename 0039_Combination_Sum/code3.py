class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        
        memo = {}
        def recur(index, target):
            
            if (index, target) not in memo:
                
                if target == 0:
                    return [[]]
                elif target < 0:
                    return []
                
                ans = []
                for i in range(index, n):
                    for ret in recur(i, target - candidates[i]):
                        ans.append([candidates[i]] + ret)
                        
                memo[index, target] = ans
                
            return memo[index, target]
        
        return recur(0, target)