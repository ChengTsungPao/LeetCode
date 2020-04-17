class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        def dfs(sindex, pindex):
            nonlocal p
            if((sindex, pindex) not in dp):
                if(sindex==len(s) and (pindex==len(p) or (p[pindex]=="*" and pindex+1==len(p)))):
                    return True
                elif((sindex==len(s)) != (pindex==len(p))):
                    return None            
                if(p[pindex]=="*"):
                    for i in range(len(s)-sindex+1):
                        ans = dfs(sindex + i, pindex + 1)    
                        if(ans): break
                else:
                    ans = (s[sindex]==p[pindex] or p[pindex]=="?") and dfs(sindex + 1, pindex + 1)
                dp[sindex, pindex] = ans
            return dp[sindex, pindex]
        
        if(len(p) > 0):
            _str = p[0]
            for i in range(1,len(p)):
                if(_str[-1]!="*" or (_str[-1]=="*" and p[i]!="*")):
                    _str += p[i]
            p = _str        

        if(dfs(0,0)):
            return True
        else:
            return False  