class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0
        nums.insert(0, 0)
        status = collections.defaultdict(int)
        for n in nums:
            s += n
            ans += status[s - k]
            status[s] += 1
        return ans