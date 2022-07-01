class BrowserHistory:

    def __init__(self, homepage: str):
        self.pageList = [homepage]
        self.currentPage = 0
        self.lastPage = 0

    def visit(self, url: str) -> None:
        self.currentPage += 1
        if self.currentPage >= len(self.pageList):
            self.pageList.append(url)
        else:
            self.pageList[self.currentPage] = url
        self.lastPage = self.currentPage

    def back(self, steps: int) -> str:
        if self.currentPage - steps <= 0 :
            self.currentPage = 0
        else:
            self.currentPage -= steps
        return self.pageList[self.currentPage]
        
    def forward(self, steps: int) -> str:
        if self.currentPage + steps >= self.lastPage:
            self.currentPage = self.lastPage
        else:
            self.currentPage += steps
        return self.pageList[self.currentPage]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)