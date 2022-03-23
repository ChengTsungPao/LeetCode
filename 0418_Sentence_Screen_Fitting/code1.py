class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        
        s = " ".join(sentence) + " "
        length = len(s)
        
        start = 0
        for _ in range(rows):
            start += cols
            # 每列超過的字母若是" "代表，可以忽略
            if s[start % length] == " ":
                start += 1
            # 每列超過的字母若不是" "代表，需要往前找，找到第一個空的位置
            else:
                while start > 0 and s[(start - 1) % length] != " ":
                    start -= 1
                    
        return start // length