class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        
        shift = 0
        
        for indice, source, target in sorted(zip(indices, sources, targets)):
            i, j = shift + indice, shift + indice + len(source)
            
            if source == s[i : j]:
                s = s[:i] + target + s[j:]
                shift += len(target) - len(source)
                
        return s