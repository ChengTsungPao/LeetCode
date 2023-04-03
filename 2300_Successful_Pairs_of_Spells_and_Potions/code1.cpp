class Solution {
public:
    vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
        int n = potions.size();
        sort(potions.begin(), potions.end());
        
        vector<int> ans;
        for(auto& spell: spells){
            int idx = lower_bound(potions.begin(), potions.end(), success / spell + (success % spell > 0)) - potions.begin();
            ans.push_back(n - idx);
        }
        
        return ans;
    }
};