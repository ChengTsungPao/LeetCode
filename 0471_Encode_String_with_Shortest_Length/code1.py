class Solution:
    def encode(self, s: str) -> str:
        
        n = len(s)
        
        candidateStrs = []
        cache = set()
        
        for length in range(1, n + 1):
            for index in range(n - length + 1):
                
                candidateStr = s[index: index + length]
                if candidateStr not in cache:
                    candidateStrs.append(candidateStr)
                    
                    _str = candidateStr
                    while len(_str) <= n:
                        cache.add(candidateStr)
                        _str += candidateStr
                        
        memo = {}
        def recur(string):
            
            if string not in memo:
                
                if len(string) <= 1:
                    return string

                ans = string
                for length in range(1, len(string) + 1):
                    string1, string2 = string[:length], string[length:]
                    
                    ans = min(ans, string1 + recur(string2), key = len)
                    for candidateStr in candidateStrs:
                        if length <= len(candidateStr):
                            continue
                            
                        count = length // len(candidateStr)
                        if count * candidateStr == string1:
                            ans = min(ans, "{}[{}]".format(count, recur(candidateStr)) + recur(string2), key = len)

                memo[string] = ans

            return memo[string]
        
        return recur(s)