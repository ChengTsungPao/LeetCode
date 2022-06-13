class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        
        '''
        S: Small
        M: Medium
        B: Big
        
        SSSSSMSSSMSSBSSSMSS
        i    k  j
        合法區間 => (i, j), (i + 1, j) ....... (k, j)
        
        k: new_valid_index
        '''
        
        ans = 0
        i = new_valid_index = -1
        for j, num in enumerate(nums):
            if num > right:
                i = j
                new_valid_index = -1
                
            if left <= num <= right:
                new_valid_index = j
                
            if new_valid_index >= 0:
                ans += (new_valid_index - i)
                
        return ans