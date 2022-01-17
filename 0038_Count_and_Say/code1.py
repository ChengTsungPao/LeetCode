class Solution:
    def countAndSay(self, n: int) -> str:
        
        def count(s):
            ans = ""
            count = 1
            s += "#"
            for i in range(1, len(s)):
                if s[i] != s[i - 1]:
                    ans += str(count) + s[i - 1]
                    count = 1
                else:
                    count += 1
            return ans
        
        ans = "1"
        for _ in range(1, n):
            ans = count(ans)
            
        return ans
  