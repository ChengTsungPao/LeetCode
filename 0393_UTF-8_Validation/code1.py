class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        '''
        規則:
            1. 長度為 1 ~ 4 bytes
            2. 若為1個字節 (1-byte)，最高位為0
            3. 若為n個字節 (n-byte)，第一個字節前n個Bit為1且第n+1個Bit為0，其餘n-1個字節前兩個Bit皆為"10"
        '''
        
        def start_ones(num):
            count = 0
            
            for _ in range(8):
                if num < 128:
                    break
                    
                num = (num - 128) << 1
                count += 1
                
            return count


        index = 0
        while index < len(data):
            count = start_ones(data[index])
            
            if count == 0:
                index += 1
                continue
            elif count == 1 or count == 8 or count > 4 or index + count - 1 >= len(data):
                return False
            
            for i in range(index + 1, index + count):
                num = data[i]

                if num < 128:
                    return False
                
                num = (num - 128) << 1
                
                if num >= 128:
                    return False
                
            index += count   
            
        return True