class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        def countDigit(number):
            count = [0] * 10
            for d in str(number):
                count[int(d)] += 1
            return count
        
        n_count = countDigit(n)
        
        maxValue = ""
        for d in range(10):
            maxValue = str(d) * n_count[d]  + maxValue
        maxValue = int(maxValue)
        
        number = 1
        while number <= maxValue:
            if n_count == countDigit(number):
                return True
            number *= 2
            
        return False