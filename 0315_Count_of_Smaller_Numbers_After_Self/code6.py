class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        '''
        概念: 找大於i的index，且滿足nums[i] > nums[j]
        想法: 當nums[i] > nums[j]且nums[k] >= nums[i]，必定滿足nums[k] > nums[j]
        '''
        
        n = len(nums)
        self.ans = [0] * n
        self.nums = [(nums[index], index) for index in range(n)]
        self.mergeSort(0, n - 1)
        return self.ans
        
        
    def mergeSort(self, left, right):
        if left == right:
            return [self.nums[left]]

        mid = left + (right - left) // 2
        leftArr = self.mergeSort(left, mid)
        rightArr = self.mergeSort(mid + 1, right)
        self.count(self.ans, leftArr, rightArr)
        return self.merge(leftArr, rightArr)
    
    
    def count(self, ans, leftArr, rightArr):
        
        m = len(leftArr)
        n = len(rightArr)
        
        i = j = rightCounter = 0
        while i < m and j < n:
            leftNum, leftIndex = leftArr[i]
            rightNum, rightIndex = rightArr[j]
            if leftNum > rightNum:
                rightCounter += 1
                j += 1
            else:
                ans[leftIndex] += rightCounter
                i += 1
                
        while i < m:
            leftNum, leftIndex = leftArr[i]
            ans[leftIndex] += rightCounter
            i += 1
        
        
    def merge(self, leftArr, rightArr):
        
        m = len(leftArr)
        n = len(rightArr)
        
        arr = []
        i = j = 0
        while i < m and j < n:
            leftNum, leftIndex = leftArr[i]
            rightNum, rightIndex = rightArr[j]
            if leftNum > rightNum:
                arr.append((rightNum, rightIndex))
                j += 1
            else:
                arr.append((leftNum, leftIndex))
                i += 1

        while i < m:
            leftNum, leftIndex = leftArr[i]
            arr.append((leftNum, leftIndex))
            i += 1

        while j < n:
            rightNum, rightIndex = rightArr[j]
            arr.append((rightNum, rightIndex))
            j += 1

        return arr