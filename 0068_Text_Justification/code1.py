class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:            
        
        def center_adjust(length, preIndex, index):
            
            if index - preIndex <= 1:
                _str = left_adjust(preIndex, index)
            else:
                _str = ""
                spacelength = [(maxWidth - length) // (index - preIndex - 1), 
                               (maxWidth - length)  % (index - preIndex - 1)]
                for i in range(preIndex, index - 1):
                    _str += words[i] + (" " * (spacelength[0] + (spacelength[1] > 0)))
                    spacelength[1] -= 1
                _str += words[index - 1]
                
            return _str
        
        def left_adjust(preIndex, index):
            
            _str = ""
            for i in range(preIndex, index - 1):
                _str += words[i] + " "
            _str += words[index - 1]
                
            return _str + " " * (maxWidth - len(_str))
            
        
        ans = []
        length = preIndex = index = 0
        
        while index < len(words):
            
            if (index - preIndex) + length + len(words[index]) <= maxWidth:
                length += len(words[index])
                index += 1
            else:
                ans.append(center_adjust(length, preIndex, index))
                index += index == preIndex
                preIndex = index
                length = 0
                
        ans.append(left_adjust(preIndex, index))
            
        return ans