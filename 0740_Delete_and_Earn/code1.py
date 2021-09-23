class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # dp[num] => 數字大小從 1 ~ num 之最大取法，其中 num = keyList[i] 而且 keyList 已排序
        #       => 來源1: 拿取與 keyList[i - 1] 組合之數字 dp[keyList[i - 1]] 若無相鄰加上 i * nums[i]
        #       => 來源2: 拿取與 keyList[i - 2] 組合之數字 dp[keyList[i - 2]] 若無相鄰加上 i * nums[i]
        #       => 來源3: 拿取與 keyList[i - 3] 組合之數字 dp[keyList[i - 2]] 若無相鄰加上 i * nums[i]
        #            ·
        #            ·
        #            ·
        #       => 來源i: 拿取與 keyList[i - i] 組合之數字 dp[keyList[i - i]] 若無相鄰加上 i * nums[i]        

        nums = collections.Counter(nums)
        keyList = sorted(list(nums.keys()))

        ans = 0
        dp = collections.defaultdict(int)
        
        for i in range(len(keyList)):
            dp[keyList[i]] = keyList[i] * nums[keyList[i]]
            for j in range(i - 1, -1, -1):
                if keyList[j] != keyList[i] - 1:
                    dp[keyList[i]] = max(dp[keyList[i]], dp[keyList[j]] + keyList[i] * nums[keyList[i]])
                
            ans = max(ans, dp[keyList[i]])
        
        return ans
