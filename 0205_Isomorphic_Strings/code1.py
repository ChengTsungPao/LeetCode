class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def status(_str):
            index = collections.defaultdict(list)
            for i in range(len(_str)):
                index[_str[i]].append(i)
            return index   
        return len(s) == len(t) and sorted(status(s).values()) == sorted(status(t).values())