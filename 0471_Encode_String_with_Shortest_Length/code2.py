class Solution:
    def encode(self, s: str) -> str:
                        
        memo = {}
        def recur(string):
            
            if string not in memo:
                
                if len(string) <= 1:
                    return string
                
                minLength = -1
                for length in range(1, len(string)):
                    s = string[:length]
                    if len(string) % length == 0 and (len(string) // length) * s == string:
                        minLength = length
                        break
                
                ans = string
                if minLength > 0:
                    ans = min(ans, "{}[{}]".format(len(string) // minLength, recur(string[:minLength])), key = len)
                    
                for i in range(1, len(string)):
                    ans = min(ans, recur(string[:i]) + recur(string[i:]), key = len)

                memo[string] = ans

            return memo[string]
        
        return recur(s)