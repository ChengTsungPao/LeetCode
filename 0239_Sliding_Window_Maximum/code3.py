class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # Step1: 紀錄每k個element的window中，左邊掃過來最大和右邊掃過來最大
        # Step2: window從start到end之最大即為max(right[start], left[end])
        
        n = len(nums)
        
        left, right = [nums[0]], [nums[-1]]
        
        for i in range(1, n):
            
            if i % k == 0:
                left.append(nums[i])
            else:
                left.append(max(nums[i], left[i - 1]))
            
            j = n - i - 1
            if (j + 1) % k == 0:
                right.append(nums[j])
            else:
                right.append(max(nums[j], right[i - 1]))
       
        right = right[::-1]

        ans = []
        for i in range(n - k + 1):
            ans.append(max(right[i], left[i + k - 1]))
            
        return ans