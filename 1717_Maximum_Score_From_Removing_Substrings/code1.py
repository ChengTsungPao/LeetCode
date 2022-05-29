class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        
        # 先拆除分數高的Substrings，因為拆除分數低的Substrings時，不可能出現分數高的Substrings
        
        def remove(_str, score):
            total_score = 0
            stack = []
            for ch in s:
                if stack and stack[-1] + ch == _str:
                    total_score += score
                    stack.pop()
                else:
                    stack.append(ch)
            return total_score, "".join(stack)
        
        if x >= y:
            scoreX, s = remove("ab", x)
            scoreY, s = remove("ba", y)
        else:
            scoreY, s = remove("ba", y)
            scoreX, s = remove("ab", x)
            
        return scoreX + scoreY