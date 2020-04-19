class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        def dfs(s1, s2, s3):
            if((s1, s2, s3) not in dp):
                dp[s1, s2, s3] = (s1=="" and s2==""       and s3==""                 ) or \
                                 (s1!="" and s1[0]==s3[0] and dfs(s1[1:], s2, s3[1:])) or \
                                 (s2!="" and s2[0]==s3[0] and dfs(s1, s2[1:], s3[1:]))   
            return dp[s1, s2, s3]
        if(len(s1)+len(s2)==len(s3) and dfs(s1, s2, s3)):
            return True
        else:
            return False