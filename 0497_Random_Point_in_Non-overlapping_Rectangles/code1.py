class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.probability_sum = []
        self.setup()
        
        
    def setup(self):
        total = 0
        areas = []
        
        for a, b, x, y in self.rects:
            width, height = abs(a - x) + 1, abs(b - y) + 1
            areas.append(width * height)
            total += areas[-1]

        self.probability_sum.append(areas[0] / total)
        for i in range(1, len(areas)):
            self.probability_sum.append(self.probability_sum[-1] + areas[i] / total)       
        
        
    def pick(self) -> List[int]:
        rectIndex = bisect.bisect_left(self.probability_sum, random.random())
        left, down, right, top = self.rects[rectIndex] 
        return [random.randrange(left, right + 1), random.randrange(down, top + 1)]
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()