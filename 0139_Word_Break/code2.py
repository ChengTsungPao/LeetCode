class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def dfs(x,index):
            if((x,index) not in dp):
                if(x==len(s)):
                    return True
                dp[x,index] = (len(s)-x>=len(wordDict[index]) and wordDict[index]==s[x:x+len(wordDict[index])] 
                               and dfs(x+len(wordDict[index]),0)) or (index<len(wordDict)-1 and dfs(x,index+1))
            return dp[x,index]
                
        if(wordDict!=[]):
            return dfs(0,0)       
        else:
            return False