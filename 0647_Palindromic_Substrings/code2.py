class Solution:
    def countSubstrings(self, s: str) -> int:
        
        new_s = "#"
        for ch in s:
            new_s += ch + "#"
        
        n = len(new_s)
        LPS = [0] * n
        
        center = 1
        center_right = 2
        
        lps_length = 0
        lps_index = 0
        
        for current_right in range(1, n):
            if current_right < center_right:
                current_left = 2 * center - current_right
                LPS[current_right] = min(LPS[current_left], center_right - current_right)
                
            # 計算以current_right為中心的LPS
            left = current_right - LPS[current_right] - 1
            right = current_right + LPS[current_right] + 1
            while left >= 0 and right < n and new_s[left] == new_s[right]:
                LPS[current_right] += 1
                left = current_right - LPS[current_right] - 1
                right = current_right + LPS[current_right] + 1
                
            if LPS[current_right] > lps_length:
                lps_length = LPS[current_right]
                lps_index = current_right
                
            # 更新center
            if current_right + LPS[current_right] >= center_right:
                center = current_right
                center_right = current_right + LPS[current_right]
        
        ans = 0
        for i in range(len(new_s)):
            if new_s[i] == "#":
                ans += LPS[i] // 2
            else:
                ans += (LPS[i] + 1) // 2
        
        return ans