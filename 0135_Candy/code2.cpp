class Solution {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        
        map<int, vector<int>> r_map;
        for(int i = 0; i < n; i++){
            int r = ratings[i];
            r_map[r].push_back(i);
        }
        
        vector<int> ans(n, 0);
        for(auto& m: r_map){
            int r = m.first;
            vector<int> indices = m.second;
            for(int i: indices){
                int candy = 1;
                if(i + 1 < n && r > ratings[i + 1]){
                    candy = max(candy, ans[i + 1] + 1);
                }
                if (i - 1 >= 0 && r > ratings[i - 1]){
                    candy = max(candy, ans[i - 1] + 1);
                }
                ans[i] = candy;
            }
        }
        
        return accumulate(ans.begin(), ans.end(), 0);
    }
};