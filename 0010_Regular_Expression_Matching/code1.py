class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        def dfs(s, p):
            if(s=="" and p==""):
                return True
            elif(s!="" and p==""):
                return None
            elif("*" not in set(p) and len(s)!=len(p)):
                return None
            
            if(len(p)>=2 and p[1]=="*"):
                if(dfs(s, p[2:])):
                    return True
                for i in range(1, len(s)+1):
                    if((p[0]=="." or s[0:i]==p[0]*i) and dfs(s[i:], p[2:])):
                        return True 
            elif(len(s)>=1 and (s[0]==p[0] or p[0]==".")):
                if(dfs(s[1:], p[1:])):
                    return True
                    
        if(dfs(s, p)):
            return True
        else:
            return False
