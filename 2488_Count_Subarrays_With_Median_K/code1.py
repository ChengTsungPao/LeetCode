class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        smaller_bigger_list = []
        for i, num in enumerate(nums):
            if num > k:
                smaller_bigger_list.append(1)
            elif num == k:
                indexk = i
                smaller_bigger_list.append(0)
            else:
                smaller_bigger_list.append(-1)
                
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + smaller_bigger_list[i - 1]
            
        oddIndexDict = collections.defaultdict(int)
        evenIndexDict = collections.defaultdict(int)
        for i in range(n, indexk, -1):
            if i % 2 == 0:
                evenIndexDict[preSum[i]] += 1
            else:
                oddIndexDict[preSum[i]] += 1
                
        ans = 0
        for i in range(indexk + 2):
            if i % 2 == 0:
                # odd + even
                ans += oddIndexDict[preSum[i]] + evenIndexDict[preSum[i] + 1]
            else:
                # odd + even 
                ans += evenIndexDict[preSum[i]] + oddIndexDict[preSum[i] + 1]
                
        return ans