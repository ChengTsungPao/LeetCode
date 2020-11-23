class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = min(strs, key = len, default = "")
        for i in range(len(strs)):
            for j in range(len(ans)):
                if strs[i][j] != ans[j]:
                    ans = strs[i][:j]
                    break            
        return ans