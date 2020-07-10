class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        dp = collections.defaultdict(list)
        def dfs(x,_str):
            nonlocal ans
            key = _str.replace(" ", "")
            if key in dp:
                anstmp = set(ans)
                for word in dp[key]:
                    if _str + word not in anstmp:
                        ans.append(_str + word)
                return ans
            if(x==len(s)):
                ans.append(_str)
                return ans
            temp = set()
            length = len(ans)
            for word in wordDict:
                if(len(s)-x>=len(word) and word==s[x:x+len(word)]):
                    if(_str==""):
                        tmp = dfs(x+len(word),_str + word)
                    else:
                        tmp = dfs(x+len(word),_str + " " + word)
                    if tmp != None:
                        for i in range(length, len(tmp)):
                            temp.add(tmp[i][len(_str):])
            dp[key] += list(temp)
            anstmp = set(ans)            
            for word in dp[key]:
                if _str + word not in anstmp:
                    ans.append(_str + word)
            return ans
                
        dfs(0,"")        
        return ans