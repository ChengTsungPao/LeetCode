class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        sorted_arr = []
        for x, y in sorted(envelopes, key = lambda x: (x[1], -x[0])):
            index = bisect.bisect_left(sorted_arr, x)
            if index < len(sorted_arr):
                sorted_arr[index] = x
            else:
                sorted_arr.append(x)
                
        return len(sorted_arr)