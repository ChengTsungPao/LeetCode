class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        pair = {}     # {leftnum: rightnum, rightnum: leftnum}
        status = {}   # {leftnum: length, rightnum: length}
        visited = set()
        
        def delete(index):
            if pair[index] != index:
                del status[index]
                del pair[index]
                
        for n in nums:
            
            if n in visited:
                continue
            else:
                visited.add(n)
            
            if n - 1 in status and n + 1 in status:
                
                left, right = pair[n - 1], pair[n + 1]
                
                combine_length = status[n - 1] + status[n + 1] + 1
                status[left] = combine_length
                status[right] = combine_length
                
                delete(n - 1)
                delete(n + 1)
                
                pair[left] = right
                pair[right] = left
                
            elif n - 1 in status:
                
                left, right = pair[n - 1], n
                
                combine_length = status[n - 1] + 1
                status[left] = combine_length
                status[right] = combine_length
                
                delete(n - 1)
                
                pair[left] = right
                pair[right] = left
                
            elif n + 1 in status:
                
                left, right = n, pair[n + 1]
                
                combine_length = status[n + 1] + 1
                status[left] = combine_length
                status[right] = combine_length
                
                delete(n + 1) 
                
                pair[left] = right
                pair[right] = left
                
            else:
                
                pair[n] = n
                status[n] = 1
                
        return max(status.values(), default = 0)
