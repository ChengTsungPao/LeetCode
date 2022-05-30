class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        
        status = collections.defaultdict(list)
        
        def getPalindrome(i, j):
            _str = ""
            while i >= 0 and j < n and s[i] == s[j]:
                _str = s[i] if i == j else s[i] + _str + s[j]
                status[i].append(_str)
                i -= 1
                j += 1
                
        for i in range(n):
            getPalindrome(i, i)
            getPalindrome(i, i + 1)
        
        dp = [[] for _ in range(n + 1)]
        dp[n] = [[]]
        
        for i in range(n - 1, -1, -1):
            for _str in status[i]:
                for ret in dp[i + len(_str)]:
                    dp[i].append([_str] + ret)
                    
        return dp[0]