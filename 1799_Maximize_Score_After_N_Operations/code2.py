class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        def gcd(a, b):
            if a < b:
                return gcd(b, a)
            if a % b == 0:
                return b
            return gcd(a % b, b)
                
        n = len(nums)
        
        ans = 0
        def recur(i, gcd_list, cache):
            nonlocal ans
            
            if i >= n:
                score = sum([(k + 1) * g for k, g in enumerate(sorted(gcd_list))])
                ans = max(ans, score)
                return
            
            if i in cache:
                recur(i + 1, gcd_list, cache)
            else:
                for j in range(i + 1, n):
                    if j not in cache:
                        recur(i + 1, gcd_list + [gcd(nums[i], nums[j])], cache | {j})
        
        recur(0, [], set())
        return ans
