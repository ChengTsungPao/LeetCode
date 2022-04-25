class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        nums = []
        counts = []
        for num in arr:
            if nums and num == nums[-1]:
                counts[-1] += 1
            else:
                nums.append(num)
                counts.append(1)
                
        
        n = len(nums)
        index = bisect.bisect_left(nums, x)
        
        choose = [0] * n
        i, j = index - 1, index
        
        while i >= 0 and j < n and k > 0:
            a, b = nums[i], nums[j]
            
            if abs(a - x) < abs(b - x):
                c = min(counts[i], k)
                choose[i] += c
                i -= 1
            elif abs(a - x) > abs(b - x):
                c = min(counts[j], k)
                choose[j] += c
                j += 1
            else:
                if a < b:
                    c = min(counts[i], k)
                    choose[i] += c
                    i -= 1
                else:
                    c = min(counts[j], k)
                    choose[j] += c
                    j += 1
            k -= c
            
        while i >= 0 and k > 0:
            c = min(counts[i], k)
            choose[i] += c
            i -= 1
            k -= c
            
        while j < n and k > 0:
            c = min(counts[j], k)
            choose[j] += c
            j += 1
            k -= c
            
        ans = []
        for i in range(n):
            ans.extend([nums[i]] * choose[i])
        
        return ans