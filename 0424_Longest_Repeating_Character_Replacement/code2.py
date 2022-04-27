class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        n = len(s)
        count = collections.defaultdict(int)

        maxLength = 0

        for i in range(n):
            count[s[i]] += 1
            
            if maxLength - max(count.values()) < k:
                maxLength += 1
            else:
                count[s[i - maxLength]] -= 1

        return maxLength