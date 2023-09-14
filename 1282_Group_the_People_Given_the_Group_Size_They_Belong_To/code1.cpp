class Solution {
public:
    vector<vector<int>> groupThePeople(vector<int>& groupSizes) {
        int n = groupSizes.size();
        
        vector<vector<int>> ans;
        unordered_map<int, vector<int>> group;
        for(int i = 0; i < n; i++){
            int s = groupSizes[i];
            
            group[s].push_back(i);
            if(group[s].size() == s){
                ans.push_back(group[s]);
                group[s] = {};
            }
        }
        
        return ans;
    }
};