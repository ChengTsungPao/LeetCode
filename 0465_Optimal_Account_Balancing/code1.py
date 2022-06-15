class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        arr = [0] * 12
        for person1, person2, price in transactions:
            arr[person1] -= price
            arr[person2] += price
            
        minStep = float("inf")
        def recur(index, step):
            nonlocal minStep
            
            if step >= minStep:
                return float("inf")
            
            if index >= 12:
                minStep = step
                return 0
            
            if arr[index] == 0:
                return recur(index + 1, step)
                        
            ans = float("inf")
            cache = set()
            for i in range(index + 1, 12):
                if arr[i] in cache or arr[i] * arr[index] >= 0:
                    continue
                cache.add(arr[i])
                
                arr[i] += arr[index]
                ans = min(ans, recur(index + 1, step + 1) + 1)
                arr[i] -= arr[index]
                
            return ans
        
        return recur(0, 0)