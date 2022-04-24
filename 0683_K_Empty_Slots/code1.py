class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:   
        
        '''
        bulbs = [6, 1, 4, 7, 2, 3, 5]
        
        [|0|, |0|, |0|, |0|, |0|,  1 , |0|] <--- day1
        [ 1 , |0|, |0|, |0|, |0|,  1 , |0|] <--- day2
        [ 1 , |0|, |0|,  1 , |0|,  1 , |0|] <--- day3
        [ 1 , |0|, |0|,  1 , |0|,  1 ,  1 ] <--- day4
        [ 1 ,  1 , |0|,  1 , |0|,  1 ,  1 ] <--- day5
        [ 1 ,  1 ,  1 ,  1 , |0|,  1 ,  1 ] <--- day6
        [ 1 ,  1 ,  1 ,  1 ,  1 ,  1 ,  1 ] <--- day7      
        '''
        
        n = len(bulbs)
        index = {}
        for i in range(1, n + 1):
            index[bulbs[i - 1]] = i
        
        ans = float("inf")
        stack = []
        for bulb in range(1, n + 1):
            while stack and index[stack[-1]] > index[bulb]:
                bulb_ = stack.pop()
                if abs(bulb_ - bulb) - 1 == k:
                    ans = min(ans, max(index[bulb_], index[bulb]))
                    
            if stack:
                bulb_ = stack[-1]
                if abs(bulb_ - bulb) - 1 == k:
                    ans = min(ans, max(index[bulb_], index[bulb]))
                    
            stack.append(bulb)
        
        return ans if ans != float("inf") else -1