class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = [-float("inf"), -float("inf")]
        for n in nums:
            if n >= ans[0]:
                ans[0] = n
            if ans[0] > ans[1]:
                ans = [ans[1], ans[0]]
        return (ans[0] - 1) * (ans[1] - 1)
