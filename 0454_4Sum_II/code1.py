class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        def combineTwoNums(nums1, nums2):
            combineNums = []
            for num1 in nums1:
                for num2 in nums2:
                    combineNums.append(num1 + num2)
            return combineNums
        
        combineNums1 = combineTwoNums(nums1, nums2)
        combineNums2 = combineTwoNums(nums3, nums4)
        
        countCombineNums2 = collections.Counter(combineNums2)
        
        ans = 0
        for combineNum1 in combineNums1:
            ans += countCombineNums2[-combineNum1]
            
        return ans