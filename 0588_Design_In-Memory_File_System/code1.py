class Node:
    def __init__(self, name):
        self.folder = name
        self.fileName = {}
        self.children = {}

class FileSystem:
    
    def __init__(self):
        self.root = Node("/")
        
    def getNames(self, path: str):
        return [folder for folder in path.split("/") if folder != ""]

    def ls(self, path: str) -> List[str]:
        node = self.root
        for folder in self.getNames(path):
            if folder not in node.children:
                return [folder] * (folder in node.fileName)
            node = node.children[folder]
        return sorted(list(node.fileName.keys()) + list(node.children.keys()))

    def mkdir(self, path: str) -> None:
        node = self.root
        for folder in self.getNames(path):
            if folder not in node.children:
                node.children[folder] = Node(folder)
            node = node.children[folder]

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        names = self.getNames(filePath)
        for folder in names[:-1]:
            node = node.children[folder]
        node.fileName[names[-1]] = node.fileName.get(names[-1], "") + content

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        names = self.getNames(filePath)
        for folder in names[:-1]:
            node = node.children[folder]
        return node.fileName[names[-1]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)