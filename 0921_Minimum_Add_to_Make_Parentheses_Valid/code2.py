class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        lack = count = 0
        
        for ch in s:
            if ch == "(":
                count += 1
            elif ch == ")" and count > 0:
                count -= 1
            else:
                lack += 1

        return count + lack