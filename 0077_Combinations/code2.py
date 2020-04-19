class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def dfs(k, s, _list):
            if(k == 0):
                ans.append(_list)
                return None
            for i in range(s, n + 1):
                dfs(k - 1, i + 1, _list + [i])
        dfs(k, 1, [])
        return ans