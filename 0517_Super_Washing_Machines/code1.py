class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        
        n = len(machines)
        total = sum(machines)
        
        if total % n > 0:
            return -1
        
        avg = total // n
        
        prefixSum = [0] * n
        suffixSum = [0] * n
        for i in range(1, n):
            prefixSum[ i] = prefixSum[ i - 1] + machines[ i - 1]
            suffixSum[~i] = suffixSum[~i + 1] + machines[~i + 1]
        
        ans = 0
        for i in range(n):
            left = avg * i - prefixSum[i] if avg * i - prefixSum[i] > 0 else 0
            right = avg * (n - i - 1) - suffixSum[i] if avg * (n - i - 1) - suffixSum[i] > 0 else 0
            ans = max(ans, left + right)
            
        return ans