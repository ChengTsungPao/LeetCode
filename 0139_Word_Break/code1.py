class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        def dfs(x,index):
            nonlocal dp
            nonlocal data
            nonlocal _str
            if((x,index) not in dp):
                if(x==len(s)):
                    return True
                dp[x,index] = (len(_str)-x>=len(data[index]) and data[index]==_str[x:x+len(data[index])] 
                               and dfs(x+len(data[index]),0)) or (index<len(data)-1 and dfs(x,index+1))
            return dp[x,index]
        
        if(len(wordDict) > 1):
            for i in range(len(wordDict)):
                dp = {}
                data = list(copy.copy(wordDict))
                _str = wordDict[i]
                del data[i]
                if(dfs(0,0)):
                    wordDict[i] = "#"
                    
        tmp = set(wordDict)
        if("#" in tmp):
            tmp.remove("#")
            data = list(tmp)
        else:
            data = wordDict
        _str = s  
        
        if(wordDict!=[]):
            dp = {}
            return dfs(0,0)       
        else:
            return False