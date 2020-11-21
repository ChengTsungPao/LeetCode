class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        for i in range(len(favoriteCompanies)):
            favoriteCompanies[i] = set(favoriteCompanies[i])
        
        for i in range(len(favoriteCompanies)):
            flag = True
            for j in range(len(favoriteCompanies)):
                if i != j and favoriteCompanies[i] & favoriteCompanies[j] == favoriteCompanies[i]:
                    flag = not flag
                    break
            if flag:
                ans.append(i)         

        return ans