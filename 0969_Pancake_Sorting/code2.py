class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        
        def flipArr(arr, num):
            idx = arr.index(num) + 1
            if idx == num:
                return []
            arr[:idx] = reversed(arr[:idx])
            arr[:num] = reversed(arr[:num])
            return [idx, num]
        
        ans = []
        for num in range(n, 0, -1):
            ans.extend(flipArr(arr, num))

        return ans