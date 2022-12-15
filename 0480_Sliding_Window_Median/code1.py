class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        from sortedcontainers import SortedList
        
        def getMediam(bst):
            n = len(bst)
            return bst[n // 2] if n % 2 == 1 else round((bst[n // 2 - 1] + bst[n // 2]) / 2, 5)
        
        ans = []
        bst = SortedList(nums[:k - 1])
        for i in range(k - 1, len(nums)):
            bst.add(nums[i])
            ans.append(getMediam(bst))
            bst.remove(nums[i - k + 1])
        
        return ans