class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(s, p):
            if((s, p) not in dp):
                if(s=="" and p==""):
                    return True
                elif(s!="" and p==""):
                    return None
                elif("*" not in set(p) and len(s)!=len(p)):
                    return None            
                if(len(p)>=2 and p[1]=="*"):
                    ans = dfs(s, p[2:])
                    for i in range(1, len(s)+1):
                        if(ans): break
                        ans = (p[0]=="." or s[0:i]==p[0]*i) and dfs(s[i:], p[2:])
                else:
                    ans = len(s)>=1 and (s[0]==p[0] or p[0]==".") and dfs(s[1:], p[1:])
                dp[s, p] = ans
            return dp[s, p]

        if(dfs(s, p)):
            return True
        else:
            return False