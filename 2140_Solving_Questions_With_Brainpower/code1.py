class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        
        @functools.lru_cache(None)
        def recur(idx):
            if idx >= n:
                return 0
            points, brainpower = questions[idx]
            return max(points + recur(idx + brainpower + 1), recur(idx + 1))
            
        return recur(0)