class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        # 只要同一個bucket裡面有兩個元素代表存在abs(nums[i] - nums[j]) <= t，所以bucket只需存一個元素
        
        bucket = {}
        t = t + 1
        
        i = 0
        j = 0
        while j < len(nums):
            num = nums[j]
            bucket_number = num // t
            
            if bucket_number in bucket:
                return True
            
            if bucket_number - 1 in bucket and abs(num - bucket[bucket_number - 1]) <= t - 1:
                return True
            
            if bucket_number + 1 in bucket and abs(bucket[bucket_number + 1] - num) <= t - 1:
                return True
            
            bucket[bucket_number] = num
            
            j += 1
            
            if j - i > k:
                del bucket[nums[i] // t]
                i += 1
        
        return False