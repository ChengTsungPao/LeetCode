class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Silding Window:
        
                [2,3,2,1]
        [3,2,1,4,7]
          [3,2,1,4,7]
            [3,2,1,4,7]
              [3,2,1,4,7]
                [3,2,1,4,7]
                  [3,2,1,4,7]
                    [3,2,1,4,7]
                      [3,2,1,4,7]
        
        '''
        
        def getMaxlength(x1, y1, x2, y2):

            max_length = 0
            cur_length = 0
            
            while x1 < y1 + 1:
                
                if nums1[x1] == nums2[x2]:
                    cur_length += 1
                else:
                    cur_length = 0
                    
                max_length = max(max_length, cur_length)
                
                x1 += 1
                x2 += 1
                
            return max_length
        
        
        ans = 0
        
        x1 = y1 = 0
        x2 = y2 = len(nums2) - 1
        
        while x1 < len(nums1):
            
            ans = max(ans, getMaxlength(x1, y1, x2, y2))
            
            if x2 == 0:
                x1 += 1
            else:
                x2 -= 1
            
            if y1 == len(nums1) - 1:
                y2 -= 1
            else:
                y1 += 1
            
        return ans