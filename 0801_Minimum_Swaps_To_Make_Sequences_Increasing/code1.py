class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        
        def swap(i, nums1, nums2):
            nums1[i], nums2[i] = nums2[i], nums1[i]
            
        def isValid(i):    
            return i - 1 < 0 or (nums1[i - 1] < nums1[i] and nums2[i - 1] < nums2[i])            
        
        memo = {}
        def recur(i, isSwap = False):

            if not isValid(i - 1):
                return float("inf")
            
            if i >= n:
                return 0
            
            if (i, isSwap) not in memo:
                # No swap
                ans = recur(i + 1, False)
                # swap
                swap(i, nums1, nums2)
                ans = min(ans, recur(i + 1, True) + 1)
                swap(i, nums1, nums2)

                memo[i, isSwap] = ans
                    
            return memo[i, isSwap]

        return recur(0)