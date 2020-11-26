class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(target, index):
            if target == 0:
                return [[]]
            elif target < 0:
                return []
            ans = []
            for i in range(index, len(candidates)):
                for nums in dfs(target - candidates[i], i):
                    ans.append([candidates[i]] + nums)
            return ans
        return dfs(target, 0)