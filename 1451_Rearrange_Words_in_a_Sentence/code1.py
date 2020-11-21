class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split(" ")
        text.sort(key = len)
        ans = text[0]
        for i in range(1, len(text)):
            ans += " " + text[i]
        return ans.capitalize()  