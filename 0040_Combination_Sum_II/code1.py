class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates = collections.Counter(candidates)
        def dfs(target, _list):
            if(target == 0):
                ans.append(_list)
            elif(target < 0):
                return None
            for n in candidates.keys():
                if(candidates[n] != 0 and ((len(_list) >= 1 and _list[-1] <= n) or len(_list) == 0)):
                    candidates[n] -= 1
                    dfs(target - n, _list + [n])
                    candidates[n] += 1
        dfs(target, [])
        return ans        