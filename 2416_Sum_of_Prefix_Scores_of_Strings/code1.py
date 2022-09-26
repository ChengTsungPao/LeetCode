class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        status = collections.defaultdict(int)
        for word in words:
            _str = ""
            for ch in word:
                _str += ch
                status[_str] += 1
        
        ans = [0] * len(words)
        for i, word in enumerate(words):
            _str = ""
            for ch in word: 
                _str += ch
                ans[i] += status[_str]
                
        return ans