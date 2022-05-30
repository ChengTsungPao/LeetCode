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
        
        memo = {}
        def recur(index):
            
            if index not in memo:
            
                if index >= n:
                    return [[]]

                ans = []
                for _str in status[index]:
                    for ret in recur(index + len(_str)):
                        ans.append([_str] + ret)
                        
                memo[index] = ans
                    
            return memo[index]
        
        return recur(0)