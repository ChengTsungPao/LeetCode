class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        
        arr = []
        ans = [1] * n
        for i, num in enumerate(obstacles):
            j = bisect.bisect_right(arr, num)
            if j >= len(arr):
                arr.append(num)
            else:
                arr[j] = num
            ans[i] = j + 1

        return ans