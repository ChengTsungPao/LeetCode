class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        # 出現在字母種類中，尋找最小且合法的開頭 (smallest lexicographical)
        
        lastIndex = {}
        for i in range(len(s)):
            lastIndex[s[i]] = i
            
        def isVaild(index):
            for value in lastIndex.values():
                if value < index:
                    return False
            return True
        
        
        ans = ""
        cur_index = 0
        
        for _ in range(len(lastIndex)):
            
            ch = "z"
            for index in range(cur_index, len(s)):
                if isVaild(index) == False:
                    break
                
                if s[index] < ch and lastIndex[s[index]] != float("inf"):
                    ch = s[index]
                    cur_index = index + 1
            
            lastIndex[ch] = float("inf")
            ans += ch
            
        return ans