class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        n = len(candidates)
        candidates.sort()
        
        memo = {}
        def recur(index, target):
            
            if (index, target) not in memo:
            
                if target == 0:
                    return [[]]
                elif target < 0:
                    return []

                ans = []
                for i in range(index, n):
                    if i == index or candidates[i - 1] < candidates[i]:
                        for ret in recur(i + 1, target - candidates[i]):
                            ans.append([candidates[i]] + ret)
                            
                memo[index, target] = ans

            return memo[index, target]
        
        return recur(0, target)