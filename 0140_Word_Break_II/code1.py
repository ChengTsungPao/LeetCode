class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        def dfs(x,index,_str):
            nonlocal dp
            if(((x,index,_str) in dp and dp[x,index,_str]!=None) or (x,index,_str) not in dp):
                if(x==len(s)):
                    ans.append(_str)
                    return True
                a = None
                b = None
                if(len(s)-x>=len(wordDict[index]) and wordDict[index]==s[x:x+len(wordDict[index])]):
                    if(_str==""):
                        a = dfs(x+len(wordDict[index]),0,_str + wordDict[index])
                    else:
                        a = dfs(x+len(wordDict[index]),0,_str + " " + wordDict[index])
                if(index<len(wordDict)-1):
                    b = dfs(x,index+1,_str)
                dp[x,index,_str] = a or b

        def check(x,index):
            nonlocal dp
            if((x,index) not in dp):
                if(x==len(s)):
                    return True
                dp[x,index] = (len(s)-x>=len(wordDict[index]) and wordDict[index]==s[x:x+len(wordDict[index])] 
                               and check(x+len(wordDict[index]),0)) or (index<len(wordDict)-1 and check(x,index+1))
            return dp[x,index]
        
        if(wordDict!=[]):
            dp = {}
            if(check(0,0)):
                dp = {}
                dfs(0,0,"")
                return ans  
            else:
                return []
        else:
            return []   