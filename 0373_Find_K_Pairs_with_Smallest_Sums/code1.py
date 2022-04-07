class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        # Kth Smallest Element in a Sorted Matrix
        
        m = len(nums1)
        n = len(nums2)
        
        ans = []
        heap = []
        index = [0] * m
        
        for i in range(m):
            heapq.heappush(heap, (nums1[i] + nums2[0], (nums1[i], nums2[0]), i))
        
        for _ in range(min(k, m * n)):
            num, pair, i = heapq.heappop(heap)
            ans.append(list(pair))
            index[i] += 1
            if index[i] < n:
                heapq.heappush(heap, (nums1[i] + nums2[index[i]], (nums1[i], nums2[index[i]]), i))
            
        return ans