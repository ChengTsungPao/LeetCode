class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        # 概念: 在merge的時候去統計rightArr比leftNum的數字小的有幾個
        
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
        return self.merge(leftArr, rightArr)
        
        
    def merge(self, leftArr, rightArr):

        arr = []
        i = j = rightCounter = 0

        while i < len(leftArr) and j < len(rightArr):
            leftNum, leftIndex = leftArr[i]
            rightNum, rightIndex = rightArr[j]
            if leftNum > rightNum:
                rightCounter += 1
                arr.append((rightNum, rightIndex))
                j += 1
            else:
                self.ans[leftIndex] += rightCounter
                arr.append((leftNum, leftIndex))
                i += 1

        while i < len(leftArr):
            leftNum, leftIndex = leftArr[i]
            self.ans[leftIndex] += rightCounter
            arr.append((leftNum, leftIndex))
            i += 1

        while j < len(rightArr):
            rightNum, rightIndex = rightArr[j]
            arr.append((rightNum, rightIndex))
            j += 1

        return arr