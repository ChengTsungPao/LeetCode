class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        total = sum(cardPoints)
        length = len(cardPoints) - k
        
        cur_sum = sum(cardPoints[:length])
        cur_min = cur_sum
        for i in range(length, len(cardPoints)):
            cur_sum += cardPoints[i]
            cur_sum -= cardPoints[i - length]
            cur_min = min(cur_min, cur_sum)
            
        return total - cur_min