class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        countDot1, countDot2 = version1.count("."), version2.count(".")
        countMax = max(countDot1, countDot2)
        version1, version2 = version1 + ".0" * (countMax - countDot1), version2 + ".0" * (countMax - countDot2)

        for v1, v2 in zip(version1.split("."), version2.split(".")):
            v1, v2 = int(v1), int(v2)
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            
        return 0