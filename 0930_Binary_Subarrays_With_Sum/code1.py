class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # prefixSum[j] - prefixSum[i] = goal => prefixSum[i] = prefixSum[j] - goal
        
        nums = [0] + nums
        
        ans = 0
        cur_sum = 0
        count = collections.defaultdict(int)
        
        for num in nums:
            cur_sum += num
            if cur_sum - goal in count:
                ans += count[cur_sum - goal] 
            count[cur_sum] += 1
        
        return ans