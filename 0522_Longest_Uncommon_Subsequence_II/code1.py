class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def getSubsequence(_str):
            dp = [""]
            for ch in _str:
                for s in dp.copy():
                    dp.append(s + ch)
            return dp
        
        count = collections.defaultdict(int)
        for _str in strs:
            for s in getSubsequence(_str):
                count[s] += 1
                
        ans = -1
        for s, c in count.items():
            if c == 1:
                ans = max(ans, len(s))
                
        return ans