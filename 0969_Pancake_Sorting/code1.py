class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        
        ans = []
        
        for length in range(len(arr), 1, -1):
            
            cur_max, maxIndex = arr[0], 0
            for index in range(1, length):
                if cur_max < arr[index]:
                    cur_max, maxIndex = arr[index], index
            
            if maxIndex == length - 1:
                continue
            
            arr[:maxIndex + 1] = reversed(arr[:maxIndex + 1])
            arr[:length] = reversed(arr[:length])
            
            ans.append(maxIndex + 1)
            ans.append(length)
            
        return ans
