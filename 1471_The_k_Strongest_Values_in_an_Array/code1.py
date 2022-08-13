class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        
        n = len(arr)
        arr.sort()
        
        m = arr[n // 2] if n % 2 else arr[n // 2 - 1]

        ans = []
        i = 0
        j = n - 1
        for _ in range(k):
            valuei, valuej = abs(arr[i] - m), abs(arr[j] - m)
            if valuei > valuej or (valuei == valuej and arr[i] > arr[j]):
                ans.append(arr[i])
                i += 1
            else:
                ans.append(arr[j])
                j -= 1
                
        return ans