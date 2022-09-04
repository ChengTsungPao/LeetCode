class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        new_p = ""
        for ch in p.lstrip("*"):
            if not new_p or ch != "*":
                new_p += ch
            elif ch == "*" and new_p[-1] != "*":
                new_p += ch
        
        memo = {}
        def recur(s, p):
            
            if (s, p) not in memo:

                if len(s) == 0 and len(p) == 0:
                    return True 

                ans = False
                if len(p) >= 2 and p[1] == "*":
                    if p[0] == ".":
                        for i in range(len(s) + 1):
                            ans = ans or recur(s[i:], p[2:])
                    else:
                        for i in range(len(s) + 1):
                            ans = ans or recur(s[i:], p[2:])    
                            if i < len(s) and s[i] != p[0]:
                                break
                elif len(s) >= 1 and len(p) >= 1 and (s[0] == p[0] or p[0] == "."):
                    ans = ans or recur(s[1:], p[1:])
                    
                memo[s, p] = ans
                    
            return memo[s, p]
        
        return recur(s, new_p)