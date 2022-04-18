# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2
            
            
        while left <= right:
            mid = left + (right - left) // 2
            
            if reader.get(mid) < target:
                left = mid + 1
            elif reader.get(mid) > target:
                right = mid - 1
            else:
                return mid
            
        return -1