class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

	# 出現在字母種類中，尋找最小且合法的開頭 (smallest lexicographical)
        
        status = {}
        for i in range(len(s)):
            status[s[i]] = i
            
        def isVaild(index):
            for value in status.values():
                if value < index:
                    return False
            return True
        
        
        ans = ""
        cur_index = 0
        
        for _ in range(len(status)):
            
            ch = "z"
            for index in range(cur_index, len(s)):
                if isVaild(index) == False:
                    break
                
                if s[index] < ch and status[s[index]] != float("inf"):
                    ch = s[index]
                    cur_index = index + 1
            
            status[ch] = float("inf")
            ans += ch
            
        return ans