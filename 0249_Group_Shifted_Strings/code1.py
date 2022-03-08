class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def getKey(string):
            shift = ord(string[0])
            key = str(0)
            for i in range(1, len(string)):
                key += "_" + str((ord(string[i]) - shift) % 26)
            return key
        
        
        status = collections.defaultdict(list)
        for string in strings:
            status[getKey(string)].append(string)
            
        return status.values()