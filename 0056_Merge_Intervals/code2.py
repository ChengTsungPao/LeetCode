class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        ans = []
        
        for start, end in intervals:
            
            left, right = bisect.bisect_left(ans, start), bisect.bisect_right(ans, end)

            if left % 2 and right % 2:
                ans[left: right] = []
            elif left % 2:
                ans[left: right] = [end]
            elif right % 2:
                ans[left: right] = [start]
            else:
                ans[left: right] = [start, end]

        return list(zip(ans[0::2], ans[1::2]))