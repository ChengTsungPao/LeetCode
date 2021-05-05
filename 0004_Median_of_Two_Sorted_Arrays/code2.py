class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def find_median(nums1, nums2, length):
            
            length = length // 2
            
            left, right = 0, len(nums1) - 1
            
            while left <= right:
                
                nums1_index = (left + right) // 2
                nums2_index = bisect.bisect_left(nums2, nums1[nums1_index]), bisect.bisect_right(nums2, nums1[nums1_index])
                
                if nums1_index + nums2_index[1] >= length >= nums1_index + nums2_index[0]:
                    return nums1_index  
                elif nums1_index + nums2_index[0] > length:
                    right = nums1_index - 1
                else:
                    left = nums1_index + 1
                    
            return -1
                    
        ans, length = 0, len(nums1) + len(nums2)
        cur_times, times = 0, 2 - length % 2
        
        while cur_times < times:
            
            index = find_median(nums1, nums2, length)
            
            if index == -1:
                nums1, nums2 = nums2, nums1
            else:
                ans += nums1[index] / times
                del nums1[index]
                length -= 1
                cur_times += 1
            
        return ans