# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        
        limit = 2 ** 31 - 1
        
        def getArrLastIndex(index):
            if reader.get(index + 1) == limit:
                return 0
            elif reader.get(index + 2) == limit:
                return 1
            
            count = 2
            while reader.get(count * count + index) != limit:
                count *= count
                
            return count + getArrLastIndex(index + count)

        
        left = 0
        right = getArrLastIndex(0)
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if reader.get(mid) < target:
                left = mid + 1
            elif reader.get(mid) > target:
                right = mid - 1
            else:
                return mid
            
        return -1