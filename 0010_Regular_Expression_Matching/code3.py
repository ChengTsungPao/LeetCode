class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        # 此題來說recur parameter用index較佳，但長遠來說用s較佳 (memo hit 頻率高)
        
        memo = {}
        def recur(s, p):
            
            if (s, p) not in memo:
            
                if not s and not p:
                    return True
                if not s or not p:
                    return len(p) % 2 == 0 and set(p[1::2]) == {"*"}

                ans = False
                if len(p) >= 2 and p[1] == "*":
                    for i in range(len(s) + 1):
                        if (p[0] != "." and s[:i] != p[0] * i) or ans: break
                        ans = recur(s[i:], p[2:])
                elif s[0] == p[0] or p[0] == ".":
                    ans = recur(s[1:], p[1:])

                memo[s, p] = ans
            
            return memo[s, p]
        
        return recur(s, p)