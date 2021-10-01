class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        # 找開頭開始最長的Palindrome
        
        return s[-1:self.longestPalindrome(s):-1] + s if len(s) > 1 else s
    
    def longestPalindrome(self, s):
        
        # Manacher's Algorithm (dp)
        # Time : O(n) 
        # Space: O(n)
        
        def maxPalindrome(i, j):
            while i >= 0 and j < len(str_) and str_[i] == str_[j]:
                i -= 1
                j += 1
            return i + 1, j - 1       
        
        # Step1: aba => #a#b#a#        
        str_ = "#"
        for s_ in s:
            str_ += s_ + "#"

        # Step2: dp[i] = max Palindrome length (包含"#")
        dp = []
        ans = 0, 0
        center = maxRight = 0
        
        for index in range(len(str_)):
            
            # 若在Palindrome範圍內可以dp
            if index < maxRight:
                # 最多只能從到"maxRight"開始搜索
                length = min(dp[2 * center - index] // 2, maxRight - index)
                newPalindrome = maxPalindrome(index - length, index + length)               
            else:
                newPalindrome = maxPalindrome(index, index)
            
            # 更新maxRight和center
            if maxRight < newPalindrome[1]:
                maxRight = newPalindrome[1]
                center = index    
                
            dp.append(newPalindrome[1] - newPalindrome[0] + 1)
            if newPalindrome[0] == 0: # 必須是從同開始的Palindrome
                ans = max(ans, newPalindrome, key = lambda x: x[1] - x[0])
            
        return (ans[1] - (str_[ans[1]] == "#")) // 2
