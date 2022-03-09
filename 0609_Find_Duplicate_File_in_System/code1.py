class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        def insertPaths(path, group):
            path = path.split(" ")
            directory = path[0]
            
            files = []
            for i in range(1, len(path)):
                splitStr = path[i].split("(")
                key = splitStr[-1][:-1]
                file = splitStr[0]
                group[key].append(directory + "/" + file)
                
        group = collections.defaultdict(list)
        for path in paths:
            insertPaths(path, group)
            
        for key in list(group.keys()):
            if len(group[key]) <= 1:
                del group[key]
            
        return group.values()