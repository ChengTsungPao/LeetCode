class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:

        ans = []
        arr = []
        
        for start, end in paint:
            i = bisect.bisect_left(arr, start)
            j = bisect.bisect_right(arr, end)
            
            s = 0
            if i % 2 and j % 2:    
                
                for k in range(i, j, 2):
                    s += arr[k + 1] - arr[k] if k + 1 < len(arr) else 0
                ans.append(s)
                
                arr[i: j] = []
                
            elif i % 2:
                if j == len(arr):
                    s += end - arr[-1]
                else:
                    s -= arr[j] - end
  
                for k in range(i, j, 2):
                    s += arr[k + 1] - arr[k] if k + 1 < len(arr) else 0

                ans.append(s)
                
                arr[i: j] = [end]
                
            elif j % 2:
                if i == len(arr): 
                    s += end - start
                else:
                    s += arr[i] - start
                    
                for k in range(i + 1, j, 2):
                    s += arr[k + 1] - arr[k] if k + 1 < len(arr) else 0

                ans.append(s)
                
                arr[i: j] = [start]
                
            else:
                if i == len(arr): 
                    s += end - start
                elif j == len(arr):
                    s += arr[i] - start
                    s += end - arr[-1]
                else:
                    s += arr[i] - start
                    s -= arr[j] - end
                
                for k in range(i + 1, j, 2):
                    s += arr[k + 1] - arr[k] if k + 1 < len(arr) else 0

                ans.append(s)
                
                arr[i: j] = [start, end]
                
        return ans