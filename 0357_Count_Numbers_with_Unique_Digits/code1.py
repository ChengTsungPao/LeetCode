class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        '''
            x => 9 + 1
           xx => 9 x 9
          xxx => 9 x 9 x 8
         xxxx => 9 x 9 x 8 x 7
        xxxxx => 9 x 9 x 8 x 7 x 6
        '''
        
        ans = 1
        count = 9
        kind = 9
        for _ in range(n):
            ans += count
            count *= kind
            kind -= 1
            
        return ans