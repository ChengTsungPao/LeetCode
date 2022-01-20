class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        
        status = collections.Counter(nums)
        sorted_num = sorted(status.keys())
        
        while sorted_num:
            
            count = status[sorted_num[0]] 
            preNum = sorted_num[0]
            del status[sorted_num[0]]
            del sorted_num[0]
            
            index = times = 0
            while times < k - 1:
                if index >= len(sorted_num) or sorted_num[index] - 1 != preNum:
                    return False
                else:
                    preNum = sorted_num[index]
                
                status[sorted_num[index]] -= count
                if status[sorted_num[index]] < 0:
                    return False
                elif status[sorted_num[index]] == 0:
                    del status[sorted_num[index]]
                    del sorted_num[index]
                else:
                    index += 1
                    
                times += 1
                
        return True