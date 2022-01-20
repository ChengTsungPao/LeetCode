class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
        def recur(index, preReplace, memo = {}):
            
            if (index, preReplace) not in memo:
            
                if index >= len(word):
                    return [""]

                ans = []

                for w in recur(index + 1, False):
                    ans.append(word[index] + w)

                if not preReplace:
                    for length in range(1, len(word) - index + 1):
                        for w in recur(index + length, not preReplace):
                            ans.append(str(length) + w)
                            
                memo[index, preReplace] = ans
                        
            return memo[index, preReplace]
        
        return recur(0, False)