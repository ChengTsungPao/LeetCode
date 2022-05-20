class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        
        def recur(arr):
            if len(arr) <= 2:
                return arr
            return recur(arr[::2]) + recur(arr[1::2])
        
        return recur(list(range(1, n + 1)))