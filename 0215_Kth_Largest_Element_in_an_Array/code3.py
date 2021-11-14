class Solution:
    
    def partition(self, arr, left, right): # 回傳pivot區間
        
        pivotIndex = random.randrange(left, right + 1, 1)
        pivot = arr[pivotIndex]
        
        # 比pivot大的往前丟
        partition_L = left
        for i in range(left, right + 1):
            if arr[i] > pivot:
                arr[partition_L], arr[i] = arr[i], arr[partition_L]
                pivotIndex = i if partition_L == pivotIndex else pivotIndex
                partition_L += 1
        arr[partition_L], arr[pivotIndex] = arr[pivotIndex], arr[partition_L]
        
        # 與pivot相等的往前丟
        partition_R = partition_L + 1
        for i in range(partition_L + 1, right + 1):
            if arr[i] == pivot:
                arr[partition_R], arr[i] = arr[i], arr[partition_R]
                partition_R += 1
        partition_R -= 1
        
        return  partition_L, partition_R
    
    
    def recur(self, arr, left, right, k):
        partition_L, partition_R = self.partition(arr, left, right)
        
        if partition_L <= k <= partition_R:
            return arr[k]
        
        if k > partition_R:
            left  = partition_R + 1
        else:
            right = partition_L - 1
            
        return self.recur(arr, left, right, k)
    
            
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.recur(nums, 0, len(nums) - 1, k - 1)
    