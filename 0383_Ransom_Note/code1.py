class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine = collections.Counter(magazine)
        ransomNote = collections.Counter(ransomNote)
        for key in ransomNote.keys():
            if ransomNote[key] > magazine[key]:
                return False
        return True