class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        # Divide And Conquer => 剔除不足k的字母，剩下的Substring在Recursion
        
        n= len(s)
        preSum = [[0] * 26 for _ in range(n + 1)]
        
        for index in range(1, n + 1):
            preSum[index][:] = preSum[index - 1][:]
            preSum[index][ord(s[index - 1]) - 97] += 1
            
        def countCharacters(i, j):
            count = []
            for a in range(26):
                count.append(preSum[j][a] - preSum[i][a])
            return count
            
        def isValid(count):
            for a in range(26):
                if 0 < count[a] < k:
                    return False
            return True
        
        def recur(i, j):
            count = countCharacters(i, j)
            if isValid(count):
                return j - i
            elif i >= j:
                return 0
            
            ans = 0
            preIndex = i
            for index in range(i + 1, j + 1):
                if 0 < count[ord(s[index - 1]) - 97] < k:
                    ans = max(ans, recur(preIndex, index - 1))
                    preIndex = index
            ans = max(ans, recur(preIndex, j))
            
            return ans
            
        return recur(0, n)