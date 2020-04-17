class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for word in strs:
            ans[str(sorted(collections.Counter(word).items()))].append(word)
        return list(ans.values())