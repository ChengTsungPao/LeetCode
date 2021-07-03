class Solution:
    def minCut(self, s: str) -> int:
        
        def isPalindrome(index, mode):
            
            if mode:
                left, right = index, index
            else:
                left, right = index, index + 1
                
            while left >= 0 and right < len(s) and s[left] == s[right]:
                status[left].append(right)
                left -= 1
                right += 1

        def recur(startindex, memo = {}):
            
            if startindex not in memo:
                
                if startindex == len(s):
                    return 0
                
                ans = float("inf")
                for nextindex in status[startindex]:
                    ans = min(ans, recur(nextindex + 1) + 1)
                    
                memo[startindex] = ans
                
            return memo[startindex]
        
        status = collections.defaultdict(list)
        for i in range(len(s)):
            isPalindrome(i, True)  # odd
            isPalindrome(i, False) # even

        return recur(0) - 1
