class FileSystem:

    def __init__(self):
        self.rootDir = {}
        
    def createPath(self, path: str, value: int) -> bool:
        folders = path[1:].split("/")
        currentDir = self.rootDir
        
        for folder in folders[:-1]:
            if folder not in currentDir:
                return False
            currentDir = currentDir[folder]
            
        if folders[-1] in currentDir:
            return False
        currentDir[folders[-1]] = {"#": value}
        return True

    def get(self, path: str) -> int:
        folders = path[1:].split("/")
        currentDir = self.rootDir
        
        for folder in folders:
            if folder not in currentDir:
                return -1
            currentDir = currentDir[folder]
        return currentDir["#"]
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)