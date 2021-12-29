# """
# This is FontInfo's API interface.
# You should not implement it, or speculate about its implementation
# """
#class FontInfo(object):
#    Return the width of char ch when fontSize is used.
#    def getWidth(self, fontSize, ch):
#        """
#        :type fontSize: int
#        :type ch: char
#        :rtype int
#        """
# 
#    def getHeight(self, fontSize):
#        """
#        :type fontSize: int
#        :rtype int
#        """
class Solution:
    def maxFont(self, text: str, w: int, h: int, fonts: List[int], fontInfo : 'FontInfo') -> int:

        def getTextWidth(text, fontSize):
            width = 0
            for ch in text:
                width += fontInfo.getWidth(fontSize, ch)
            return width
        
        left = 0
        right = len(fonts) - 1
        while right >= 0:
            if fontInfo.getHeight(fonts[right]) <= h:
                break
            right -= 1
        
        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            value = getTextWidth(text, fonts[mid])
            if value > w:
                right = mid - 1
            else:
                ans = fonts[mid]
                left = mid + 1
        
        return ans