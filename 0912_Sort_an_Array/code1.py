class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)
    
    def mergeSort(self, nums, left, right):
        if left == right:
            return [nums[left]]
        
        mid = left + (right - left) // 2
        sorted_left = self.mergeSort(nums, left, mid)
        sorted_right = self.mergeSort(nums, mid + 1, right)
        
        return self.merge(sorted_left, sorted_right)
    
    def merge(self, sorted_left, sorted_right):
        
        m = len(sorted_left)
        n = len(sorted_right)
        
        arr = []
        i = j = 0
        while i < m and j < n:
            if sorted_left[i] <= sorted_right[j]:
                arr.append(sorted_left[i])
                i += 1
            else:
                arr.append(sorted_right[j])
                j += 1
                
        while i < m:
            arr.append(sorted_left[i])
            i += 1
            
        while j < n:
            arr.append(sorted_right[j])
            j += 1
            
        return arr