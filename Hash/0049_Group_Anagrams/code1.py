class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # sort char by counting sort
        def sortWord(word):
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord("a")] += 1
            sortedWord = ""
            for i, c in enumerate(count):
                sortedWord += chr(i + ord("a")) * c
            return sortedWord
        
        group = collections.defaultdict(list)
        for word in strs:
            sortedWord = sortWord(word)
            group[sortedWord].append(word)
            
        return group.values()