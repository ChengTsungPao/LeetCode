class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:           
        if(nums2!=[]):
            for i in range(m-1,-1,-1):
                nums1[i + n] = nums1[i]
            index1, index2 = n, 0
            for i in range(m + n):
                if(index2 >= n  or (index1 < m + n and nums1[index1] < nums2[index2])):
                    nums1[i] = nums1[index1]
                    index1 += 1
                else:
                    nums1[i] = nums2[index2]
                    index2 += 1