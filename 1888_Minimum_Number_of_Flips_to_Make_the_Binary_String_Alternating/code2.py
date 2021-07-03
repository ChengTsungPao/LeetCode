class Solution:
    def minFlips(self, s: str) -> int:
        
        # 若字串長度為偶數，則"Pick"的操作毫無意義，單純只是奇偶交換
        # 若字串長度為奇數，則"Pick"的操作意義為首位數字維持奇數，其他奇偶交換
        
        odd, even = collections.defaultdict(int), collections.defaultdict(int)
        
        for i in range(len(s)):
            if i % 2 == 0:
                odd[s[i]] += 1
            else:
                even[s[i]] += 1

        ans = min(odd["0"] + even["1"], odd["1"] + even["0"])

        if len(s) % 2 == 1:
            
            for i in range(len(s)):
                odd[s[i]] -= 1
                even[s[i]] += 1
                odd, even = even, odd
                ans = min(ans, odd["0"] + even["1"], odd["1"] + even["0"])
                
        return ans
