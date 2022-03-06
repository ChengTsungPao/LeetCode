# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        visited = set()
        hostname = startUrl[7:].split("/")[0]
        
        def recur(startUrl):
            if startUrl in visited:
                return []
            
            visited.add(startUrl)
            
            ret = [startUrl]
            for url in htmlParser.getUrls(startUrl):
                if hostname not in url:
                    continue
                ret.extend(recur(url))
            return ret

        return recur(startUrl)