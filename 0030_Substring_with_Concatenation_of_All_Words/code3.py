class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:    
        ans, length, total_length = [], len(words[0]), len(words[0]) * len(words)
        words = collections.Counter(words)
        
        for start in range(length):
            find, left, right = collections.Counter([]), start, start + length
            while left + total_length <= len(s):
                word = s[right - length : right]
                if word in words:
                    find[word] += 1
                    while find[word] > words[word]:
                        find[s[left : left + length]] -= 1
                        left += length
                else:
                    left = right
                    find = collections.Counter([])
                if find == words:
                    ans.append(left)
                    find[s[left : left + length]] -= 1
                    left += length
                right += length
                
        return ans