class Solution:
    def maxProduct(self, words: List[str]) -> int:     
        num = []
        for s in words:
            num.append(set(s))
        
        ans = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if(num[i]&num[j]==set() and len(words[i])*len(words[j]) > ans):
                    ans = len(words[i])*len(words[j])
        
        return ans        