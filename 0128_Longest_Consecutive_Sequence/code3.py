class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        ans = 0
        que = set(nums)
        
        while que:
            num = que.pop()
            
            count = 1
            cur_num = num
            while cur_num + 1 in que:
                que.remove(cur_num + 1)
                cur_num += 1
                count += 1
                
            cur_num = num
            while cur_num - 1 in que:
                que.remove(cur_num - 1)
                cur_num -= 1
                count += 1
                
            ans = max(ans, count)
            
        return ans
