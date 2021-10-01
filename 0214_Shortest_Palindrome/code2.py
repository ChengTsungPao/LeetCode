class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # 先記錄reverse字串的結果，找開頭開始最長的Palindrome
        
        _s = s[::-1]
        for i in range(len(s), -1, -1):
            if s[:i] == _s[len(s) - i:]:
                return _s[:len(s) - i] + s     