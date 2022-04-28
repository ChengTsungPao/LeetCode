class Solution:
    def compress(self, chars: List[str]) -> int:
        
        n = len(chars)

        target = chars[0]
        count = i = j = 0
        
        for j in range(n):
            ch = chars[j]
            
            if ch == target:
                count += 1
            else:
                chars[i] = target
                i += 1
                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                count = 1
                target = ch
            
        chars[i] = target
        i += 1
        if count > 1:
            for digit in str(count):
                chars[i] = digit
                i += 1
            
        return i