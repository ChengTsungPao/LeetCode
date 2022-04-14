class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
        
    def quickSort(self, nums, i, j):
        if i >= j:
            return

        left, right = self.partition(nums, i, j)
        self.quickSort(nums, i, left - 1)
        self.quickSort(nums, right + 1, j)
        
    def partition(self, nums, i, j):
        pivotIndex = random.randrange(i, j + 1)
        pivot = nums[pivotIndex]
        nums[pivotIndex], nums[j] = nums[j], nums[pivotIndex]

        left = i
        for index in range(i, j):
            if nums[index] < pivot:
                nums[index], nums[left] = nums[left], nums[index]
                left += 1
                
        right = left
        for index in range(left, j):
            if nums[index] == pivot:
                nums[index], nums[right] = nums[right], nums[index]
                right += 1
        nums[j], nums[right] = nums[right], nums[j]
        return left, right