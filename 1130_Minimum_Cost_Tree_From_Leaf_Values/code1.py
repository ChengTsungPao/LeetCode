class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
                
        n = len(arr)
        
        memo = {}
        def recur(i, j):
            
            if (i, j) not in memo:
            
                if i == j:
                    return arr[i], 0
            
                max_ = sum_ = float("inf")
                
                for k in range(i, j):
                    leftMax, leftSum = recur(i, k)
                    rightMax, rightSum = recur(k + 1, j)
                    total = leftSum + rightSum + leftMax * rightMax

                    if sum_ > total or (sum_ == total and max_ > max(leftMax, rightMax)):
                        max_ = max(leftMax, rightMax)
                        sum_ = total
                        
                memo[i, j] = max_, sum_
                    
            return memo[i, j]
                
        return recur(0, n - 1)[1]