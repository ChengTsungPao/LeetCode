class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        a = 0
        for i in range(1, len(horizontalCuts)):
            a = max(a, abs(horizontalCuts[i] - horizontalCuts[i - 1]))
        b = 0
        for i in range(1, len(verticalCuts)):
            b = max(b, abs(verticalCuts[i] - verticalCuts[i - 1]))
        return (a * b) % 1000000007