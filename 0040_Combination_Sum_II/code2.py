class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = collections.Counter(candidates)
        number = list(candidates.keys())
        def dfs(target, index):
            if target == 0:
                return [[]]
            elif target < 0:
                return []
            ans = []
            for i in range(index, len(number)):
                if candidates[number[i]] != 0:
                    candidates[number[i]] -= 1
                    for nums in dfs(target - number[i], i):
                        ans.append([number[i]] + nums)
                    candidates[number[i]] += 1
            return ans
        return dfs(target, 0) 