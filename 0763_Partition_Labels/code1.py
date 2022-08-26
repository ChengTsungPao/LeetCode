class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        n = len(s)

        lastIndex  = [0] * 26
        for index, ch in enumerate(s):
            lastIndex[ord(ch) - ord("a")] =  index
        
        cut = [0]
        maxIndex = 0
        for index, ch in enumerate(s):
            
            if index > maxIndex:
                cut.append(index)
                maxIndex = index
                
            maxIndex = max(maxIndex, lastIndex[ord(ch) - ord("a")])
            
        cut.append(n)

        return [cut[i + 1] - cut[i] for i in range(len(cut) - 1)]