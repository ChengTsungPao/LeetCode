class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        '''
        規則:
            1. 長度為 1 ~ 4 bytes
            2. 若為1個字節 (1-byte)，最高位為0
            3. 若為n個字節 (n-byte)，第一個字節前n個Bit為1且第n+1個Bit為0，其餘n-1個字節前兩個Bit皆為"10"
        '''
        
        countOnes = 0
        
        for d in data:
            if countOnes == 0:
                if d >> 3 == 0b11110:
                    countOnes = 3
                elif d >> 4 == 0b1110:
                    countOnes = 2
                elif d >> 5 == 0b110:
                    countOnes = 1
                elif d >> 7 == 0b0:
                    countOnes = 0
                else:
                    return False
            else:
                if d >> 6 != 0b10:
                    return False
                countOnes -= 1
                
        return countOnes == 0
