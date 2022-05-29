class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        n = len(tokens)
        tokens.sort()
        
        ans = score = 0
        i, j = 0, n - 1
        
        while i <= j and score >= 0:
            
            while i <= j and power - tokens[i] >= 0:
                power -= tokens[i]
                score += 1
                i += 1
                
            ans = max(ans, score)
            
            power += tokens[j]
            score -= 1
            j -= 1
            
        return ans