class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        
        def condition(guess):
            count = curSum = 0
            for s in sweetness:
                curSum += s
                if curSum >= guess:
                    count += 1
                    curSum = 0
            return count >= k + 1
        
        left = 0
        right = sum(sweetness) + 1
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                left = mid + 1
            else:
                right = mid
                
        return left - 1