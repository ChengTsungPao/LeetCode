class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        '''
        kadane's algorithm
            當 sum_ = nums[i: j + 1] < 0 時，會想要從前面的 i 再往前縮，不過不管怎麼縮 sum_ 都會是負的
            (可以把sum_想成利潤，既然到目前為止錢都被敗光了，那前面的 i 再往前縮，利潤仍然是負的)
        
        '''
        
        ans = -float("inf")
        sum_ = 0
        for num in nums:
            sum_ += num
            ans = max(ans, sum_)
            
            if sum_ < 0:
                sum_ = 0
                
        return ans